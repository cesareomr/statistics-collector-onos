/*
 * Copyright 2018-present Open Networking Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package uah.tfg;

import org.apache.felix.scr.annotations.*;
import org.onosproject.net.*;
import org.onosproject.net.device.DeviceService;
import org.onosproject.net.device.PortStatistics;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.*;
import java.util.concurrent.TimeUnit;
import org.w3c.dom.DOMImplementation;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Text;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;


@Component(immediate = true)
public class AppComponent
{
    private final Logger log = LoggerFactory.getLogger(getClass());

    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    public DeviceService deviceService;
    //Devuelve información acerca del estado de los enlaces
    //@Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    //private LinkService linkService; /*!< @brief Servicio para interactuar con el inventario de enlaces */

    @Activate
    protected void activate() throws Exception
    {
        log.info("activate - INFO 0 | Entro en el método activate");
        ArrayList keyPort = new ArrayList();
        ArrayList valueBytesR = new ArrayList();
        ArrayList valueBytesS = new ArrayList();
        ArrayList valueDuration = new ArrayList();
        ArrayList valuePacketsR = new ArrayList();
        ArrayList valuePacketsRxD = new ArrayList();
        ArrayList valuePacketsRxE = new ArrayList();
        ArrayList valuePacketsS = new ArrayList();
        ArrayList valuePacketsTxD = new ArrayList();
        ArrayList valuePacketsTxE = new ArrayList();

        for (int siempre=0 ; siempre <20 ; siempre++)   //Temporal para que pueda acabar
        {    //Para que fuera infinito lo haría con un while, pero no consigo pararlo
            log.info("activate - INFO 1 | Llamo al método generateStatistics");
            generateStatistics(keyPort, valueBytesR, valueBytesS, valueDuration, valuePacketsR, valuePacketsRxD, valuePacketsRxE, valuePacketsS, valuePacketsTxD, valuePacketsTxE);
            keyPort.clear();
            valueBytesR.clear();
            valueBytesS.clear();
            valueDuration.clear();
            valuePacketsR.clear();
            valuePacketsRxD.clear();
            valuePacketsRxE.clear();
            valuePacketsS.clear();
            valuePacketsTxD.clear();
            valuePacketsTxE.clear();
            TimeUnit.SECONDS.sleep(10); //No puede ser menor que 3
        }
    }

    public void generateStatistics(ArrayList keyP,ArrayList valueBR,ArrayList valueBS,ArrayList valueD
            ,ArrayList valuePR,ArrayList valuePRD,ArrayList valuePRE,ArrayList valuePS,ArrayList valuePTD,ArrayList valuePTE)
    {
        log.info("generateStatistics - INFO 0 | Entro en el método generateStatistics");
        Iterable<Device> devices = deviceService.getAvailableDevices(Device.Type.SWITCH);   //Almaceno en la variable devices todos los switchs que hay en la red
        String switchs[] = new String[50];      //Para guarda el id de cada switch
        String nombreOriginal;
        int a =0;

        for (Device d : devices)    //Recorro todos los switchs
        {
            List<Port> ports = deviceService.getPorts(d.id());      //Almaceno en la variable ports, todos los puertos del switch


            for (Port port : ports)     //Obtengo estadisticas para cada puerto de cada switch
            {
                PortStatistics portstat = deviceService.getStatisticsForPort(d.id(), port.number());

                if (portstat != null)
                {
                    nombreOriginal=d.id().toString();
                    switchs[a]=reemplaza(nombreOriginal);       //Le quito los ':' para que no me de error al generar el XML
                    a++;
                    keyP.add(port.number().toString());
                    valueBR.add(Long.toString(portstat.bytesReceived()));
                    valueBS.add(Long.toString(portstat.bytesSent()));
                    valueD.add(Long.toString(portstat.durationSec()));
                    valuePR.add(Long.toString(portstat.packetsReceived()));
                    valuePRD.add(Long.toString(portstat.packetsRxDropped()));
                    valuePRE.add(Long.toString(portstat.packetsRxErrors()));
                    valuePS.add(Long.toString(portstat.packetsSent()));
                    valuePTD.add(Long.toString(portstat.packetsTxDropped()));
                    valuePTE.add(Long.toString(portstat.packetsTxErrors()));
                }
                else
                {
                    log.info("generateStatistics - INFO 1 | No se pueden recuperar estadisticas del puerto: " + port.number() + "del switch: " +d.id().toString());
                }
            }
        }

        try
        {
            log.info("generateStatistics - INFO 1 | Generando resultado.xml");
            generateXML(switchs, keyP, valueBR, valueBS, valueD , valuePR, valuePRD, valuePRE, valuePS, valuePTD, valuePTE);
        } catch (Exception e)
        {
            log.info("generateStatistics - ERROR 0 | Error al generar *.xml");
            log.info(e.getMessage());
        }
    }

    public void generateXML(String switchID[], ArrayList<String> keyP, ArrayList<String> valueBR, ArrayList<String> valueBS
            , ArrayList<String> valueD, ArrayList<String> valuePR, ArrayList<String> valuePRD, ArrayList<String> valuePRE
            , ArrayList<String> valuePS, ArrayList<String> valuePTD, ArrayList<String> valuePTE) throws Exception
    {
        log.info("generateXML - INFO 0 | Entro en el metodo generate");

        if(keyP.isEmpty())
        {
            log.info("generateXML - ERROR 0 | No se ha definido puerto");
            return;
        }
        else
        {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            DOMImplementation implementation = builder.getDOMImplementation();
            Document document = implementation.createDocument(null, "home", null);
            document.setXmlVersion("1.0");

            Element raiz = document.getDocumentElement();	//Nodo principal
            for(int i=0; i<keyP.size();i++)	       //Por cada key creamos un item que contendrá la key y el value
            {
                Element itemNode = document.createElement(switchID[i]);
                Element keyNode = document.createElement("port");
                Text nodeKeyValue = document.createTextNode(keyP.get(i));
                keyNode.appendChild(nodeKeyValue);
                Element valueNode = document.createElement("bytesR");
                Text nodeValueValue = document.createTextNode(valueBR.get(i));
                valueNode.appendChild(nodeValueValue);
                Element valueNode1 = document.createElement("bytesS");
                Text nodeValueValue1 = document.createTextNode(valueBS.get(i));
                valueNode1.appendChild(nodeValueValue1);
                Element valueNode2 = document.createElement("duration");
                Text nodeValueValue2 = document.createTextNode(valueD.get(i));
                valueNode2.appendChild(nodeValueValue2);
                Element valueNode3 = document.createElement("packetsR");
                Text nodeValueValue3 = document.createTextNode(valuePR.get(i));
                valueNode3.appendChild(nodeValueValue3);
                Element valueNode4 = document.createElement("packetsRxD");
                Text nodeValueValue4 = document.createTextNode(valuePRD.get(i));
                valueNode4.appendChild(nodeValueValue4);
                Element valueNode5 = document.createElement("packetsRxE");
                Text nodeValueValue5 = document.createTextNode(valuePRE.get(i));
                valueNode5.appendChild(nodeValueValue5);
                Element valueNode6 = document.createElement("packetsS");
                Text nodeValueValue6 = document.createTextNode(valuePS.get(i));
                valueNode6.appendChild(nodeValueValue6);
                Element valueNode7 = document.createElement("packetsTxD");
                Text nodeValueValue7 = document.createTextNode(valuePTD.get(i));
                valueNode7.appendChild(nodeValueValue7);
                Element valueNode8 = document.createElement("packetsTxE");
                Text nodeValueValue8 = document.createTextNode(valuePTE.get(i));
                valueNode8.appendChild(nodeValueValue8);
                itemNode.appendChild(keyNode);
                itemNode.appendChild(valueNode);
                itemNode.appendChild(valueNode1);
                itemNode.appendChild(valueNode2);
                itemNode.appendChild(valueNode3);
                itemNode.appendChild(valueNode4);
                itemNode.appendChild(valueNode5);
                itemNode.appendChild(valueNode6);
                itemNode.appendChild(valueNode7);
                itemNode.appendChild(valueNode8);
                raiz.appendChild(itemNode);
            }

            Source source = new DOMSource(document);
            Result result = new StreamResult(new java.io.File("/home/cesareo/Resultados/resultado.xml"));
            Transformer transformer = TransformerFactory.newInstance().newTransformer();
            transformer.transform(source, result);
            log.info("generateXML - OK 0 | Se ha generado resultado.xml exitosamente");
        }
    }

    public String reemplaza(String nombre)
    {
        return(nombre.replace(":","_"));
    }

    @Deactivate
    protected void deactivate()
    {
        log.info("deactivate - INFO 0 | Entro en el método deactivate");
    }
}