 endpoint (address: 0x%02x), ignoring the new one
      sanei_usb_open: we already have a int-out endpoint (address: 0x%02x), ignoring the new one
     sanei_usb_open: we already have a bulk-in endpoint (address: 0x%02x), ignoring the new one
     sanei_usb_open: we already have a bulk-out endpoint (address: 0x%02x), ignoring the new one
    sanei_usb_open: we already have a isochronous-in endpoint (address: 0x%02x), ignoring the new one
      sanei_usb_open: we already have a isochronous-out endpoint (address: 0x%02x), ignoring the new one
     sanei_usb_open: we already have a control-in endpoint (address: 0x%02x), ignoring the new one
  sanei_usb_open: we already have a control-out endpoint (address: 0x%02x), ignoring the new one
 sanei_usb_open: open of `%s' failed: %s
        sanei_usb_open: fcntl of `%s' failed: %s
       sanei_usb_open: can't open device `%s': usbcalls support missing
       sanei_usb_open: access method %d not implemented
       sanei_usb_open: opened usb device `%s' (*dn=%d)
        sanei_usb_open: found interrupt-%s endpoint (address 0x%02x)
   sanei_usb_open: found bulk-%s endpoint (address 0x%02x)
        sanei_usb_open: found isochronous-%s endpoint (address 0x%02x)
 sanei_usb_open: found control-%s endpoint (address 0x%02x)
     sanei_usb_read_bulk: size == NULL
      sanei_usb_read_bulk: dn >= device number || dn < 0
     sanei_usb_read_bulk: trying to read %lu bytes
  sanei_usb_read_bulk: read failed: %s
   sanei_usb_read_bulk: can't read without a bulk-in endpoint
     sanei_usb_read_bulk: usbcalls support missing
  sanei_usb_read_bulk: access method %d not implemented
  sanei_usb_read_bulk: read returned EOF
 sanei_usb_read_bulk: wanted %lu bytes, got %ld bytes
   sanei_usb_write_bulk: size == NULL
     sanei_usb_write_bulk: dn >= device number || dn < 0
    sanei_usb_write_bulk: trying to write %lu bytes
        sanei_usb_write_bulk: write failed: %s
 sanei_usb_write_bulk: can't write without a bulk-out endpoint
  sanei_usb_write_bulk: usbcalls support missing
 sanei_usb_write_bulk: access method %d not implemented
 sanei_usb_write_bulk: wanted %lu bytes, wrote %ld bytes
        sanei_usb_control_msg: dn >= device number || dn < 0, dn=%d
    sanei_usb_control_msg: rtype = 0x%02x, req = %d, value = %d, index = %d, len = %d
      sanei_usb_control_msg: SCANNER_IOCTL_CTRLMSG error - %s
        sanei_usb_control_msg: libusb complained: %s
   sanei_usb_control_msg: usbcalls support missing
        sanei_usb_control_msg: access method %d not implemented
        sanei_usb_read_int: size == NULL
       sanei_usb_read_int: dn >= device number || dn < 0
      sanei_usb_read_int: trying to read %lu bytes
   sanei_usb_read_int: access method %d not implemented
   sanei_usb_read_int: can't read without an int endpoint
 sanei_usb_read_int: usbcalls support missing
   sanei_usb_read_int: read returned EOF
  sanei_usb_read_int: wanted %lu bytes, got %ld bytes
    sanei_usb_set_configuration: dn >= device number || dn < 0, dn=%d
      sanei_usb_set_configuration: configuration = %d
        sanei_usb_set_configuration: libusb complained: %s
     sanei_usb_set_configuration: access method %d not implemented
  sanei_usb_claim_interface: dn >= device number || dn < 0, dn=%d
        sanei_usb_claim_interface: device dn=%d is missing
     sanei_usb_claim_interface: interface_number = %d
       sanei_usb_claim_interface: libusb complained: %s
       sanei_usb_claim_interface: access method %d not implemented
    sanei_usb_release_interface: dn >= device number || dn < 0, dn=%d
      sanei_usb_release_interface: device dn=%d is missing
   sanei_usb_release_interface: interface_number = %d
     sanei_usb_release_interface: libusb complained: %s
     sanei_usb_release_interface: access method %d not implemented
  sanei_usb_set_altinterface: dn >= device number || dn < 0, dn=%d
       sanei_usb_set_altinterface: alternate = %d
     sanei_usb_set_altinterface: libusb complained: %s
      sanei_usb_set_altinterface: access method %d not implemented
   sanei_usb_close: evaluating environment variable SANE_USB_WORKAROUND
   sanei_usb_close: workaround: %d
        sanei_usb_close: closing device %d
     sanei_usb_close: dn >= device number || dn < 0
 sanei_usb_close: device %d already closed or never opened
      sanei_usb_close: usbcalls support missing
      sanei_usb_clear_halt: evaluating environment variable SANE_USB_WORKAROUND
      sanei_usb_clear_halt: dn >= device number || dn < 0
    sanei_usb_clear_halt: workaround: %d
   sanei_usb_clear_halt: BULK_IN ret=%d
   sanei_usb_clear_halt: BULK_OUT ret=%d
  sanei_usb_get_descriptor: dn >= device number || dn < 0, dn=%d
 sanei_usb_get_descriptor: libusb error: %s
             �e���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���f���e���e���e���e�� f��f�� f��0f��@f��Pf��`f��pf���e��libusb_scan_devices             sanei_usb_scan_devices  sanei_usb_exit  sanei_usb_init sanei_thread func() done - status = %d
 setting SIGPIPE to SIG_IGN
 sanei_thread_waitpid() - %ld
 * thread has been canceled!
 * result = %d (%p)
 * detaching thread(%ld)
 restoring SIGPIPE to SIG_DFL
        thread started, calling func() now...
  sanei_thread_kill() will kill %ld
      pthread_create() failed with %d
        pthread_create() created thread %ld
    sanei_thread_sendsig() %d to thread (id=%ld)
           �                                                               mustek_usb2 attach_one_scanner: enter
 AutoLevel: start
 AutoLevel: init data is over
 AutoLevel: exit
 LLF_CALCULATEMOTORTABLE:Exit
 Color48 Color24 Gray16 Gray8 Lineart Reflective Positive Negative calc_parameters: end
 Asic_Reset: Enter
 Asic_Reset: Exit
 Transparent_GetRows: call in
 WriteIOControl Error!
 RegisterBankStatus=%d
 Mustek_SendData: write error
 SetRWSize: Enter
 SetRWSize: Exit
 SetExtraSetting:Enter
 wCCD_PixelNumber=%d
 bThreshold=%d
 SetExtraSetting:Exit
 FF_SCAN_IMAGE_OPTION=0x%x
 SetPackAddress:Enter
 channel gap=%d
 CISPackAreaStartAddress=%d
 InValidPixelNumber=%d
 Set Invalid Pixel ok
 F5_ScanDataFormat=0x%x
 SetScanMode():Exit
 SetLEDTime:Enter
 SetLEDTime:Exit
 Asic_TurnLamp: Enter
 Lamp0 PWM = %d
 Asic_TurnLamp: Exit
 Asic_TurnTA: Enter
 Lamp1 PWM = %d
 Asic_TurnTA: Exit
 Mustek_ClearFIFO:Enter
 Mustek_ClearFIFO:Exit
 LLFSetRamAddress:Enter
 LLFSetRamAddress:Exit
 SetAFEGainOffset:Exit
 Asic_SetAFEGainOffset:Enter
 Asic_SetAFEGainOffset: Exit
 Asic_ScanStart: Enter
 Asic_ScanStart: Exit
 Mustek_DMAWrite: write error
 Mustek_DMAWrite: Exit
 Mustek_DMARead: Enter
 Mustek_DMARead: read error
 Mustek_DMARead: Exit
 LLFRamAccess:Enter
 end steal 2 byte!
 LLFRamAccess:Exit
 LLFSetMotorTable:Enter
 LLFSetMotorTable:Exit
 Asic_ReadImage: Exit
 OpenScanChip:Enter
 OpenScanChip: Exit
 SetLineTimeAndExposure:Enter
 SetLineTimeAndExposure:Exit
 CCDTiming:Enter
 Dpi=%d
 CCDTiming:Exit
 Asic_SetShadingTable:Enter
 wValidPixelNumber = %d
 lpShadingTable == NULL
 Asic_SetShadingTable: Exit
 Asic_ScanStop: Enter
 Asic_ScanStop: Exit
 MotorPhase=0x%x
 Asic_Close: Enter
 CloseScanChip:Enter
 CloseScanChip: Exit
 Asic_Close: Exit
 GetChipStatus:Enter
 Mustek_ReceiveData
 GetChipStatus:Exit
 Asic_WaitUnitReady:Enter
 WaitChipIdle:Error!
 Wait %d s
 Asic_WaitUnitReady: Exit
 Asic_Open: Enter
 chip has been opened. fd=%d
 Asic_Open: no scanner found
 Asic_WaitUnitReady
 SafeInitialChip:Enter
 isFirstOpenChip=%d
 DRAM_Test:Enter
 Mustek_DMAWrite error
 DRAM Test error...(No.=%d)
 DRAM_Text: Exit
 SafeInitialChip: exit
 DRAM_Test: Error
 Asic_Open: not enough memory
 Asic_Open: Exit
 Asic_SetCalibrate: Enter
 wNowMotorDPI=%d
 isMotorMove=%d
 MotorSyncPixelNumber=%d
 wScanAccSteps=%d
 BeforeScanFixSpeedStep=%d
 byScanDecSteps=%d
 BackTrackFixSpeedStep=%d
 wMultiMotorStep=%d
 TotalStep=%d
 Motor Time = %d
 Motor Time Over Flow !!!
 Asic_SetCalibrate: Exit
 IsCarriageHome:Enter
 IsCarriageHome:Error!
 LampHome=%d
 IsCarriageHome:Exit
 LLFMotorMove:Enter
 Set start/end pixel
 AccStep=%d
 FixMoveSteps=%d
 DecStep=%d
 FixMoveSpeed=%d
 ACTION_TYPE_BACKTOHOME
 Forward or Backward
 ACTION_TYPE_BACKWARD
 ACTION_TYPE_TEST_MODE
 motor_steps=%d
 LOBYTE(motor_steps)=%d
 HIBYTE(motor_steps)=%d
 Asic_WaitCarriageHome:Enter
 Asic_WaitCarriageHome: Exit
 LLFMotorMove:Exit
 MotorBackHome:Enter
 MotorBackHome:Exit
 Asic_MotorMove:Enter
 Asic_MotorMove: Exit
 Asic_SetWindow: Enter
 dwBytesCountPerRow = %d
 SetMotorStepTable:Enter
 CalculateMotorTable:Enter
 CalculateMotorTable:Exit
 SetMotorCurrent:Enter
 SetMotorCurrent:Exit
 Asic_SetWindow: Exit
 SetMotorStepTable:Exit
 Asic_CarriageHome:Enter
 Asic_CarriageHome: Exit
 Asic_IsTAConnected: Enter
 hasTA=%d
 Asic_IsTAConnected():Exit
 Asic_SetMotorType:Enter
 Asic_SetMotorType: Exit
 Reflective_AdjustAD: call in
 Asic_SetSource: Enter
 Asic_SetSource: Source error
 Asic_SetSource: Exit
 != == sane_init: start
 sane-backends 1.0.27 sane_init: authorize %s null
 sane_init: exit
 sane_exit: start
 sane_exit: exit
 GetDeviceStatus: start
 Mustek BearPaw 2448 TA Pro flatbed scanner sane_get_devices: exit
 MustScanner_Init: Call in
 Asic_Initialize:Enter
 InitTiming:Enter
 InitTiming:Exit
 Asic_Initialize: Exit
 PowerControl: start
 CarriageHome: start
 init_options: start
 Number of options Scan Mode Scan mode Scan source StopScan: start
 StopScan: exit
 Scan resolution preview Preview Debugging Options auto-warmup Automatic warmup Enhancement threshold Threshold gamma-value Gamma value Geometry tl-x Top-left x tl-y Top-left y br-x Bottom-right x br-y Bottom-right y init_options: exit
 sane_open: exit
 sane_close: start
 sane_close: exit
 set get unknown set_auto sane_control_option: exit
 sane_get_parameters: start
 sane_get_parameters: exit
 sane_start: start
 SetParameters: start
 Reflective_Reset: call in
 Reflective_Reset: exit
 Transparent_Reset: call in
 MustScanner_Prepare: call in
 SetParameters: exit
 GetParameters: start
 GetParameters: exit
 sane_start : read_rows = %d
 warming up: %d
 SCANNING ... 
 StartScan: start
 sane_start: exit
 sane_cancel: start
 sane_cancel: Scan finished
 Reflective_StopScan: call in
 sane_cancel: do nothing
 sane_cancel: exit
 sane_read: start: max_len=%d
 sane_read: handle is null!
 sane_read: buf is null!
 sane_read: len is null!
 ReadScannedData: start
 Reflective_GetRows: call in 
 sane_read :after memcpy
 sane_read: after %d
 sane_read : get *len = %d
 sane_read: exit
 mustek-A2nu2 BearPaw 2448TA Pro   attach_one_scanner: devname = %s
       AutoLevel: iHeight = %d, iWidth = %d
   AutoLevel: Find min , max is over!
     AutoLevel: Set min , max is over!
      LLF_CALCULATEMOTORTABLE:Enter
  calc_parameters : preview set ScanMode SM_RGB24
        calc_parameters : preview set ScanMode SM_GRAY
 calc_parameters :scan Source = %s
      sane_star:sane params .format = %d
     MustScanner_GetRgb48BitLine1200DPI: call in 
   MustScanner_GetRgb48BitLine1200DPI: thread create
      MustScanner_GetRgb48BitLine1200DPI: thread exit
        MustScanner_GetRgb48BitLine1200DPI: leave MustScanner_GetRgb48BitLine1200DPI
   MustScanner_GetRgb48BitLine: call in 
  MustScanner_GetRgb48BitLine: thread create
     MustScanner_GetRgb48BitLine: thread exit
       MustScanner_GetRgb48BitLine: leave MustScanner_GetRgb48BitLine
 MustScanner_GetRgb24BitLine1200DPI: call in
    MustScanner_GetRgb24BitLine1200DPI: thread create
      MustScanner_GetRgb24BitLine1200DPI: g_dwTotalTotalXferLines=%d
 MustScanner_GetRgb24BitLine1200DPI: g_Height=%d
        MustScanner_GetRgb24BitLine1200DPI: thread exit
        MustScanner_GetRgb24BitLine1200DPI: leave MustScanner_GetRgb24BitLine1200DPI
   MustScanner_GetRgb24BitLine: call in
   MustScanner_GetRgb24BitLine: get wWantedTotalLines= %d
 MustScanner_GetRgb24BitLine: thread create
     MustScanner_GetRgb24BitLine: !isOrderInvert
    MustScanner_GetRgb24BitLine: thread exit
       MustScanner_GetRgb24BitLine: g_dwTotalTotalXferLines=%d,g_SWHeight=%d
  MustScanner_GetRgb24BitLine: g_SWBytesPerRow=%d
        MustScanner_GetRgb24BitLine: isOrderInvert is TRUE
     MustScanner_GetRgb24BitLine: before byRed
      MustScanner_GetRgb24BitLine: before byGreen
    MustScanner_GetRgb24BitLine: before byBlue
     MustScanner_GetRgb24BitLine: before set lpLine
 MustScanner_GetRgb24BitLine: i=%d
      MustScanner_GetRgb24BitLine: leave MustScanner_GetRgb24BitLine
 MustScanner_GetMono16BitLine: call in
  MustScanner_GetMono16BitLine: thread create
    MustScanner_GetMono16BitLine: thread exit
      MustScanner_GetMono16BitLine: leave MustScanner_GetMono16BitLine
       MustScanner_GetMono1BitLine1200DPI: call in
    MustScanner_GetMono1BitLine1200DPI: thread create
      MustScanner_GetMono1BitLine1200DPI: thread exit
        MustScanner_GetMono1BitLine1200DPI: leave MustScanner_GetMono1BitLine1200DPI
   MustScanner_GetMono1BitLine: call in
   MustScanner_GetMono1BitLine: thread create
     MustScanner_GetMono1BitLine: thread exit
       MustScanner_GetMono1BitLine: leave MustScanner_GetMono1BitLine
 MustScanner_GetMono8BitLine: call in
   MustScanner_GetMono8BitLine: thread create
     MustScanner_GetMono8BitLine: thread exit
       MustScanner_GetMono8BitLine: leave MustScanner_GetMono8BitLine
 MustScanner_GetMono8BitLine1200DPI: call in
    MustScanner_GetMono8BitLine1200DPI: thread create
      MustScanner_GetMono8BitLine1200DPI: thread exit
        MustScanner_GetMono8BitLine1200DPI: free the before line data!
 MustScanner_GetMono8BitLine1200DPI: leave MustScanner_GetMono8BitLine1200DPI
   MustScanner_GetMono16BitLine1200DPI: call in
   MustScanner_GetMono16BitLine1200DPI: thread create
     MustScanner_GetMono16BitLine1200DPI: thread exit
       MustScanner_GetMono16BitLine1200DPI: free before line data!
    MustScanner_GetMono16BitLine1200DPI: leave MustScanner_GetMono16BitLine1200DPI
 Mustek_WriteAddressLineForRegister: Enter
      Mustek_WriteAddressLineForRegister: Exit
       Mustek_SendData: Enter. reg=%x,data=%x
 ChannelR_StartPixel=%d,ChannelR_EndPixel=%d
    read out pixel over max pixel! image will shift!!!
     set CISPackAreaStartAddress ok
 CISPackAreaStartAddress + (SegmentTotalPixel*(PackAreaUseLine*1))=%d
   PackAreaUseLine=%d,TotalLineShift=%d
   SetScanMode():Enter; set f5 register
   Asic_TurnLamp: Scanner is not opened
   Asic_TurnTA: Scanner is not opened
     Asic_ScanStart: Scanner is not opened
  Mustek_DMAWrite: Enter:size=%d
 Asic_ReadCalibrationData: Enter
        Asic_ReadCalibrationData: Scanner is not scanning
      Asic_ReadCalibrationData: Can't malloc bCalBuffer memory
       Asic_ReadCalibrationData: Exit
 MustScanner_ReadDataFromScanner: call in, and in new thread
    MustScanner_ReadDataFromScanner: wWantedLines=%d
       MustScanner_ReadDataFromScanner: wScanLinesThisBlock=%d
        Asic_ReadImage: Enter : LinesCount = %d
        Asic_ReadImage: Scanner is not scanning
        Asic_ReadImage: chip->dwBytesCountPerRow = %d
  Asic_ReadImage: dwXferBytes == 0
       MustScanner_ReadDataFromScanner:Asic_ReadImage return error
    MustScanner_ReadDataFromScanner:thread exit
    MustScanner_ReadDataFromScanner: Read image ok
 MustScanner_ReadDataFromScanner: thread exit
   MustScanner_ReadDataFromScanner: leave MustScanner_ReadDataFromScanner
 Alloc a new shading table= %d Byte!
    Asic_ScanStop: Stop scan error
 Asic_ScanStop: Clear scan error
        Asic_ScanStop: DMAReadGeneralMode error
        LLFSetMotorCurrentAndPhase:Enter
       LLFSetMotorCurrentAndPhase:Exit
        Asic_Close: Scanner is not opened
      Asic_Close: Scanner is scanning, try to stop scanning
  Asic_Close: CloseScanChip error
        Asic_WaitUnitReady: Scanner has not been opened
        Asic_Open: sanei_usb_find_devices failed: %s
   Asic_Open: sanei_usb_open of %s failed: %s
     Asic_Open: OpenScanChip error
  %d,%d,%d,%d,%d,%d,%d,%d,%d,%d
  Asic_Open: SafeInitialChip error
       Asic_Open: device %s successfully opened
       bScanBits=%d,wXResolution=%d, wYResolution=%d,	wX=%d, wY=%d, wWidth=%d, wLength=%d
     Asic_SetCalibrate: Scanner is not opened
       Asic_SetCalibrate: insufficiency memory!
       malloc LLF_MOTORMOVE =%ld Byte
 wPerLineNeedBufferSize=%d,BytePerPixel=%d,dwBytesCountPerRow=%d
        wPerLineNeedBufferSize=%d,wLength=%d
   wThinkCCDResolution=%d,wCCD_PixelNumber=%d
     dwLineWidthPixel=%d,wYResolution=%d
    Find Boundary CCDDummyCycleNumber == %d
        XRatioTypeDouble=%.2f,XRatioAdderDouble=%.2f,XRatioTypeWord=%d
 wScanAccSteps=%d,byScanDecSteps=%d
     BeforeScanFixSpeedStep=%d,BackTrackFixSpeedStep=%d
     isMotorMoveToFirstLine=%d,isUniformSpeedToScan=%d,isScanBackTracking=%d
        StartSpeed =%d, EndSpeed = %d
  (SANE_Byte)((motor_steps & 0x00ff0000) >> 16)=%d
       bScanBits=%d,wXResolution=%d,wYResolution=%d,wX=%d,wY=%d,wWidth=%d,wLength=%d
  Asic_SetWindow: Scanner is not opened
  EndSpeed = %d, BytesCountPerRow=%d, MotorCurrentTable=%d, LinePixelReport=%d
   MustScanner_BackHome: call in 
 MustScanner_BackHome: Asic_Open return error
   MustScanner_BackHome: Asic_CarriageHome return error
   MustScanner_BackHome: Asic_WaitUnitReady return error
  MustScanner_BackHome: leave  MustScanner_BackHome
      MustScanner_PowerControl: Call in
      MustScanner_PowerControl: Asic_Open return error
       MustScanner_PowerControl: Asic_TurnLamp return error
   MustScanner_PowerControl: Asic_IsTAConnected return error
      MustScanner_PowerControl: Asic_TurnTA return error
     MustScanner_PowerControl: leave MustScanner_PowerControl
       Reflective_FindTopLeft: call in
        Reflective_FindTopLeft: scanner has been opened
        Reflective_FindTopLeft: scanner not prepared
   Reflective_FindTopLeft: lpCalData malloc error
 Reflective_FindTopLeft: Asic_ScanStart return error
    Reflective_FindTopLeft: Asic_ReadCalibrationData return error
  Reflective_FindTopLeft: *lpwStartY = %d, *lpwStartX = %d
       Reflective_FindTopLeft: leave Reflective_FindTopLeft
   Transparent_FindTopLeft: call in
       Transparent_FindTopLeft: scanner not opened
    Transparent_FindTopLeft: scanner not prepared
  Transparent_FindTopLeft: lpCalData malloc fail
 Transparent_FindTopLeft: *lpwStartY = %d, *lpwStartX = %d
      Transparent_FindTopLeft: leave Transparent_FindTopLeft
 Reflective_LineCalibration16Bits: call in
      Reflective_LineCalibration16Bits: scanner not opened
   Reflective_LineCalibration16Bits: scanner not prepared
 Reflective_LineCalibration16Bits: lpWhiteData or lpDarkData malloc error 
      Reflective_LineCalibration16Bits: Asic_SetCalibrate return error 
      Reflective_LineCalibration16Bits: Asic_ScanStart return error 
 Reflective_LineCalibration16Bits: Asic_SetMotorType return error 
      Reflective_LineCalibration16Bits: Asic_TurnLamp return error 
  Reflective_LineCalibration16Bits: Asic_ReadCalibrationData return error 
       Reflective_LineCalibration16Bits: malloc error 
        Reflective_LineCalibration16Bits: wCalWidth = %d, wCalHeight = %d
      Reflective_LineCalibration16Bits: leave Reflective_LineCalibration16Bits
       Transparent_AdjustAD: call in
  Transparent_AdjustAD: run in first adjust offset do-while
      Transparent_AdjustAD: RGain=%d, ROffset=%d, RDir=%d  GGain=%d, GOffset=%d, GDir=%d  BGain=%d, BOffset=%d, BDir=%d
      Transparent_AdjustAD: MaxR=%d, MinR=%d  MaxG=%d, MinG=%d  MaxB=%d, MinB=%d
     Transparent_AdjustAD: leave Transparent_AdjustAD
       Reflective_AdjustAD: scanner has been opened
   Reflective_AdjustAD: scanner not prepared
      Reflective_AdjustAD: lpCalData malloc error
    Reflective_AdjustAD: run in first adjust offset do-while
       Reflective_AdjustAD: run out first adjust offset do-while
      Reflective_AdjustAD: 					   g_chip.AD.OffsetR=%d,					   g_chip.AD.OffsetG=%d,					   g_chip.AD.OffsetB=%d
    Reflective_AdjustAD: g_chip.AD.GainR = %d,g_chip.AD.GainG = %d,g_chip.AD.GainB = %d
    Reflective_AdjustAD: RGain=%d, ROffset=%d, RDir=%d  GGain=%d, GOffset=%d, GDir=%d  BGain=%d, BOffset=%d, BDir=%d
       Reflective_AdjustAD: MaxR=%d, MinR=%d  MaxG=%d, MinG=%d  MaxB=%d, MinB=%d
      Reflective_AdjustAD: run in second adjust offset do-while
      Reflective_AdjustAD:after ad gain
      Reflective_AdjustAD: leave Reflective_AdjustAD
 Asic_SetSource: Source is Reflect
      Asic_SetSource: Source is Position
     Asic_SetSource: Source is Negtive
      SANE Mustek USB2 backend version %d.%d build %d from %s
        sane_get_devices: start: local_only = %s
       MustScanner_GetScannerState: Asic_Open return error
    sane_open: start :devicename = %s
      MustScanner_Init: Asic_Open return error
       MustScanner_Init: leave MustScanner_Init
       Read-only option that specifies how many options a specific devices supports.   Selects the scan mode (e.g., lineart, monochrome, or color).    Selects the scan source (such as a document-feeder).    Sets the resolution of the scanned image.       Request a preview-quality scan. Warm-up until the lamp's brightness is constant instead of insisting on 40 seconds warm-up time.        Select minimum-brightness to get a white point  Sets the gamma value of all channels.   Top-left x position of scan area.       Top-left y position of scan area.       Bottom-right x position of scan area.   Bottom-right y position of scan area.   sane_get_option_descriptor: option = %s (%d)
   sane_control_option: start: action = %s, option = %s (%d)
      sane_control_option: don't call this function while scanning
   sane_control_option: option %d >= NUM_OPTIONS || option < 0
    sane_control_option: option %d is inactive
     sane_control_option: can't get unknown option %d
       sane_control_option: option %d is not settable
 sane_control_option: sanei_constrain_value returned %s
 sane_control_option: can't set unknown option %d
       sane_control_option: unknown action %d for option %d
   sane_get_parameters :params.format = %d
        sane_get_parameters :params.depth = %d
 sane_get_parameters :params.pixels_per_line = %d
       sane_get_parameters :params.bytes_per_line = %d
        sane_get_parameters :params.lines = %d
 sane_start: top left x >= bottom right x --- exiting
   sane_start: top left y >= bottom right y --- exiting
   Sane_start:setpara ,setpara.fmArea.x1=%d
       Sane_start:setpara ,setpara.fmArea.x2=%d
       Sane_start:setpara ,setpara.fmArea.y1=%d
       Sane_start:setpara ,setpara.fmArea.y2=%d
       Sane_start:setpara ,setpara.pfPixelFlavor=%d
   Sane_start:setpara ,setpara.wLinearThreshold=%d
        Sane_start:setpara ,setpara.wTargetDPI=%d
      Sane_start:setpara ,setpara.smScanMode=%d
      Sane_start:setpara ,setpara.ssScanSource =%d
   Sane_start:setpara ,setpara.pGammaTable =%p
    Reflective_Reset: scanner has been opened
      Reflective_Reset: Asic_Open return error
       Reflective_Reset: Asic_Reset return error
      Reflective_Reset: Asic_SetSource return error
  Reflective_Reset: Asic_TurnLamp return error
   Reflective_Reset: Asic_Close return error
      Transparent_Reset: scanner has been opened
     Transparent_Reset: can not open scanner
        Reflective_Reset: Asic_TurnTA return error
     Transparent_Reset: leave Transparent_Reset
     SetParameters: ScanSource error
        SetParameters: PixelFlavor error
       SetParameters: x1 > x2, error
  SetParameters: y1 >= y2, error
 SetParameters: x2 > MAX_SCANNING_WIDTH, error
  SetParameters: y2 > MAX_SCANNING_HEIGHT, error
 SetParameters: g_tiTarget.wDpi=%d
      SetParameters: g_tiTarget.wX=%d
        SetParameters: g_tiTarget.wY=%d
        SetParameters: g_tiTarget.wWidth=%d
    SetParameters: g_tiTarget.wHeight=%d
   MustScanner_Prepare: Asic_Open return error
    MustScanner_Prepare: Asic_WaitUnitReady return error
   MustScanner_Prepare:ScanSource is SS_Reflective
        MustScanner_Prepare: Asic_TurnLamp return error
        MustScanner_Prepare: Asic_SetSource return error
       MustScanner_Prepare:ScanSource is SS_Positive
  MustScanner_Prepare: Asic_TurnTA return error
  MustScanner_Prepare:ScanSource is SS_Negative
  MustScanner_Prepare: Asic_SetSource return good
        MustScanner_Prepare: leave MustScanner_Prepare
 SetParameters: MustScanner_Prepare fail
        SetParameters: LinearThreshold error
   SetParameters: IN gamma table not NULL
 SetParameters: gamma table malloc %ld Bytes
    SetParameters: address of g_pGammaTable=%p
     SetParameters: gamma table malloc fail
 SetParameters: set g_pGammaTable to NULL
       Reflective_ScanSuggest: call in
        Reflective_ScanSuggest: pTarget->wDpi = %d
     Reflective_ScanSuggest: pSuggest->wXDpi = %d
   Reflective_ScanSuggest: pSuggest->wYDpi = %d
   Reflective_ScanSuggest: pTarget->wX = %d
       Reflective_ScanSuggest: pTarget->wY = %d
       Reflective_ScanSuggest: pTarget->wWidth = %d
   Reflective_ScanSuggest: pTarget->wHeight = %d
  Reflective_ScanSuggest: pSuggest->wX = %d
      Reflective_ScanSuggest: pSuggest->wY = %d
      Reflective_ScanSuggest: pSuggest->wWidth = %d
  Reflective_ScanSuggest: pSuggest->wHeight = %d
 Reflective_ScanSuggest: wMaxWidth = %d
 Reflective_ScanSuggest: wMaxHeight = %d
        Reflective_ScanSuggest: g_Width=%d
     Reflective_ScanSuggest: again, g_Width=%d
      Reflective_ScanSuggest: pSuggest->dwBytesPerRow = %d
   Reflective_ScanSuggest: leave Reflective_ScanSuggest
   Transparent_ScanSuggest: call in
       Transparent_ScanSuggest: isOptimalSpeed  is true
       Transparent_ScanSuggest: isOptimalSpeed  not true
      Transparent_ScanSuggest: leave Transparent_ScanSuggest
 sane_start: sane_params.format = %d
    StartScan: g_ScanType==ST_Reflective
   Reflective_SetupScan: Call in
  Reflective_SetupScan: scanner has been opened
  Reflective_SetupScan: scanner not prepared
     Reflective_SetupScan: Asic_Open return error
   Reflective_SetupScan: Asic_Open successfully
   Reflective_SetupScan: Reflective_AdjustAD return error
 Reflective_SetupScan: Reflective_AdjustAD successfully
 after find top left,g_X=%d,g_Y=%d
      before line calibration,g_X=%d,g_Y=%d
  Reflective_SetupScan: Reflective_LineCalibration16Bits return error
    Reflective_SetupScan: after Reflective_LineCalibration16Bits,g_X=%d,g_Y=%d
     Reflective_SetupScan: before Asic_SetWindow
    Reflective_SetupScan: g_bScanBits=%d, g_XDpi=%d, g_YDpi=%d, g_X=%d, g_Y=%d, g_Width=%d, g_Height=%d
    Reflective_SetupScan: leave Reflective_SetupScan
       Reflective_PrepareScan:g_wtheReadyLines=%d
     Reflective_PrepareScan:g_lpReadImageHead malloc %d Bytes
       Reflective_PrepareScan: g_lpReadImageHead malloc error 
        StartScan: g_ScanType==ST_Transparent
  Transparent_SetupScan: call in
 Transparent_SetupScan: scanner has been opened
 Transparent_SetupScan: scanner not prepared
    Transparent_SetupScan: g_YDpi=%d
       Transparent_SetupScan: g_wLineDistance=%d
      Transparent_SetupScan: g_wPixelDistance=%d
     Transparent_SetupScan: Asic_Open return error
  Transparent_SetupScan: Asic_TurnLamp return error
      Transparent_SetupScan: Asic_IsTAConnected return error
 Transparent_SetupScan: no TA device
    Transparent_SetupScan: Asic_TurnTA return error
        Transparent_SetupScan: after find top and left g_X=%d, g_Y=%d
  Transparent_SetupScan: before line calibration,g_X=%d,g_Y=%d
   Transparent_LineCalibration16Bits: call in
     Transparent_LineCalibration16Bits: scanner not opened
  Transparent_LineCalibration16Bits: scanner not prepared
        Transparent_LineCalibration16Bits: lpWhiteData or lpDarkData malloc fail
       Transparent_LineCalibration16Bits: malloc fail
 Transparent_LineCalibration16Bits: wCalWidth = %d, wCalHeight = %d
     Transparent_LineCalibration16Bits: leave Transparent_LineCalibration16Bits
     Transparent_SetupScan: after Reflective_LineCalibration16Bits,g_X=%d,g_Y=%d
    Transparent_SetupScan: g_bScanBits=%d, g_XDpi=%d, g_YDpi=%d, g_X=%d, g_Y=%d, g_Width=%d, g_Height=%d
   Transparent_SetupScan: leave Transparent_SetupScan
     Transparent_PrepareScan: call in
       Transparent_PrepareScan:malloc fail
    Transparent_PrepareScan: leave Transparent_PrepareScan
 sane_cancel: warning: is scanning
      Reflective_StopScan: scanner not opened
        Reflective_StopScan: scanner not prepared
      Reflective_StopScan: thread exit
       Reflective_StopScan: leave Reflective_StopScan
 Transparent_StopScan: call in
  Transparent_StopScan: thread exit
      Transparent_StopScan: leave Transparent_StopScan
       sane_read: scan was cancelled, is over or has not been initiated yet
   sane_read: before read data read_row=%d
        sane_read: buffer size is %ld
  ReadScannedData: wanted Rows = %d
      Reflective_GetRows: scanner not opened 
   