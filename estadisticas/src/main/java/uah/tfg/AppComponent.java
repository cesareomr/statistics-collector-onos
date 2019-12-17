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
import org.onosproject.net.link.LinkService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.*;

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
    //Quizas con este saque mas datos
    //@Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    //private LinkService linkService; /*!< @brief Servicio para interactuar con el inventario de enlaces */

    @Activate
    protected void activate() throws Exception
    {
        log.info("activate - INFO 0 | Entro en el método activate");
        Iterable<Device> devices = deviceService.getAvailableDevices(Device.Type.SWITCH);   //Almaceno en la variable devices todos los switchs que hay en la red
        ArrayList key = new ArrayList();
        ArrayList value = new ArrayList();
        int i=0, servicios=2;

        for (Device d : devices)    //Recorro todos los switch
        {
            List<Port> ports = deviceService.getPorts(d.id());      //Almaceno en la variable ports, todos los puertos del switch

            for (Port port : ports)     //Obtengo estadisticas para cada puerto
            {
                PortStatistics portstat = deviceService.getStatisticsForPort(d.id(), port.number());

                if (portstat != null) {
                    log.info("Paquetes recibidos: " + portstat.packetsReceived());
                    items[i] = d.id().toString();
                    key.add(port.number().toString());
                    value.add(Long.toString(portstat.bytesReceived()));
                    i++;
                } else {
                    log.info("No se pueden recuperar estadisticas del puerto: " + port.number());
                }
            }
        }
            try {
                log.info("activate - INFO 1 | Generando " + nombreArchivo + ".xml");
                generate(nombreArchivo, key, value);    //Llamada al método generate
            } catch (Exception e) {
            }

    }

    public void generateBytes(ArrayList key, ArrayList value)
    {
        log.info(" generateBytes - INFO 0 | Entro en el método generateBytes");
        Iterable<Device> devices = deviceService.getAvailableDevices(Device.Type.SWITCH);   //Almaceno en la variable devices todos los switchs que hay en la red

        for (Device d : devices)    //Recorro todos los switch
        {
            List<Port> ports = deviceService.getPorts(d.id());      //Almaceno en la variable ports, todos los puertos del switch

            for (Port port : ports)     //Obtengo estadisticas para cada puerto
            {
                PortStatistics portstat = deviceService.getStatisticsForPort(d.id(), port.number());

                if (portstat != null)
                {
                    key.add(port.number().toString());
                    value.add(Long.toString(portstat.bytesReceived()));
                } else
                    {
                    log.info(" generateBytes - INFO 1 | No se pueden recuperar estadisticas del puerto: " + port.number() + "del switch: " +d.id().toString());
                }
            }
        }

        try
        {
            log.info("generateBytes - INFO 1 | Generando bytes.xml");
            generate("bytes", key, value);    //Llamada al método generate
        } catch (Exception e)
        {
            log.info("generaBytes - ERROR 0 | Error al generar bytes.xml");
        }
    }

    public void generateBytes(ArrayList key, ArrayList value)
    {
        log.info(" generateBytes - INFO 0 | Entro en el método generateBytes");
        Iterable<Device> devices = deviceService.getAvailableDevices(Device.Type.SWITCH);   //Almaceno en la variable devices todos los switchs que hay en la red

        for (Device d : devices)    //Recorro todos los switch
        {
            List<Port> ports = deviceService.getPorts(d.id());      //Almaceno en la variable ports, todos los puertos del switch

            for (Port port : ports)     //Obtengo estadisticas para cada puerto
            {
                PortStatistics portstat = deviceService.getStatisticsForPort(d.id(), port.number());

                if (portstat != null)
                {
                    key.add(port.number().toString());
                    value.add(Long.toString(portstat.bytesReceived()));
                } else
                {
                    log.info(" generateBytes - INFO 1 | No se pueden recuperar estadisticas del puerto: " + port.number() + "del switch: " +d.id().toString());
                }
            }
        }

        try
        {
            log.info("generateBytes - INFO 1 | Generando bytes.xml");
            generate("bytes", key, value);    //Llamada al método generate
        } catch (Exception e)
        {
            log.info("generaBytes - ERROR 0 | Error al generar bytes.xml");
        }
    }

    //public static void generate(String name, ArrayList<String> key,ArrayList<String> value) throws Exception
    public void generate(String name, ArrayList<String> key, ArrayList<String> value) throws Exception
    {
        log.info("generate - INFO 0 | Entro en el método generate");
        if(key.isEmpty() || value.isEmpty() || key.size()!=value.size())
        {
            log.info("generate - ERROR 0 | Error en la dupla clave-valor");
            return;
        }
        else
        {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            DOMImplementation implementation = builder.getDOMImplementation();
            Document document = implementation.createDocument(null, name, null);
            document.setXmlVersion("1.0");

            Element raiz = document.getDocumentElement();	//Nodo principal

            for(int i=0; i<key.size();i++)	       //Por cada key creamos un item que contendrá la key y el value
            {
                Element itemNode = document.createElement(name);  //Esta parte se puede mejorar
                Element keyNode = document.createElement("port");
                Text nodeKeyValue = document.createTextNode(key.get(i));
                keyNode.appendChild(nodeKeyValue);
                Element valueNode = document.createElement("value");
                Text nodeValueValue = document.createTextNode(value.get(i));
                valueNode.appendChild(nodeValueValue);
                itemNode.appendChild(keyNode);
                itemNode.appendChild(valueNode);
                raiz.appendChild(itemNode);
            }
            Source source = new DOMSource(document);
            Result result = new StreamResult(new java.io.File(name+".xml")); 	//nombre del archivo
            Transformer transformer = TransformerFactory.newInstance().newTransformer();
            transformer.transform(source, result);
            log.info("generate - OK 0 | Se ha generado " +name +".xml exitosamente");
        }
    }

    @Deactivate
    protected void deactivate()
    {
        log.info("deactivate - INFO 0 | Entro en el método deactivate");
    }
}