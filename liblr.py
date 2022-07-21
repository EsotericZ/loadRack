import sys
import time
import traceback
from Phidget22.Devices.VoltageRatioInput import VoltageRatioInput
from Phidget22.PhidgetException import PhidgetException
from Phidget22.Phidget import Phidget
from Phidget22.Net import Net

try:
    # TODO: fix this to be explicit on imports!
    from PhidgetHelperFunctions import *
except ImportError:
    sys.stderr.write("\nCould not find PhidgetHelperFunctions. Either add PhdiegtHelperFunctions.py to your project folder "
                      "or remove the import from your project.")
    sys.stderr.write("\nPress ENTER to end program.")
    readin = sys.stdin.readline()
    sys.exit()

"""
* Configures the device's DataInterval and ChangeTrigger.
* Displays info about the attached Phidget channel.
* Fired when a Phidget channel with onAttachHandler registered attaches
*
* @param self The Phidget channel that fired the attach event
"""
def onAttachHandler(self):

    ph = self
    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information

        # print("\nAttach Event:")

        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            # print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
            #     "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel:  " + str(channel) + "\n")
        # else:
            # print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
            #         "\n\t-> Channel:  " + str(channel) + "\n")

        """
        * Set the DataInterval inside of the attach handler to initialize the device with this value.
        * DataInterval defines the minimum time between VoltageRatioChange events.
        * DataInterval can be set to any value from MinDataInterval to MaxDataInterval.
        """
        # print("\n\tSetting DataInterval to 1000ms")
        ph.setDataInterval(1000)

        """
        * Set the VoltageRatioChangeTrigger inside of the attach handler to initialize the device with this value.
        * VoltageRatioChangeTrigger will affect the frequency of VoltageRatioChange events, by limiting them to only occur when
        * the voltage ratio changes by at least the value set.
        """
        # print("\tSetting Voltage Ratio ChangeTrigger to 0.0")
        ph.setVoltageRatioChangeTrigger(0.0)

        """
        * Set the SensorType inside of the attach handler to initialize the device with this value.
        * You can find the appropriate SensorType for your sensor in its User Guide and the VoltageRatioInput API
        * SensorType will apply the appropriate calculations to the voltage ratio reported by the device
        * to convert it to the sensor's units.
        * SensorType can only be set for Sensor Port voltage ratio inputs (VINT Ports and Analog Input Ports)
        """
        if(ph.getChannelSubclass() == ChannelSubclass.PHIDCHSUBCLASS_VOLTAGERATIOINPUT_SENSOR_PORT):
            print("\tSetting VoltageRatio SensorType")
            ph.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_VOLTAGERATIO)


    except PhidgetException as e:
        print("\nError in Attach Event:")
        DisplayError(e)
        traceback.print_exc()
        return

"""
* Displays info about the detached Phidget channel.
* Fired when a Phidget channel with onDetachHandler registered detaches
*
* @param self The Phidget channel that fired the attach event
"""
def onDetachHandler(self):

    ph = self

    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information

        print("\nDetach Event:")

        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel:  " + str(channel) + "\n")
        else:
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel:  " + str(channel) + "\n")

    except PhidgetException as e:
        print("\nError in Detach Event:")
        DisplayError(e)
        traceback.print_exc()
        return


"""
* Writes Phidget error info to stderr.
* Fired when a Phidget channel with onErrorHandler registered encounters an error in the library
*
* @param self The Phidget channel that fired the attach event
* @param errorCode the code associated with the error of enum type ph.ErrorEventCode
* @param errorString string containing the description of the error fired
"""
def onErrorHandler(self, errorCode, errorString):

    sys.stderr.write("[Phidget Error Event] -> " + errorString + " (" + str(errorCode) + ")\n")

"""
* Outputs the VoltageRatioInput's most recently reported voltage ratio.
* Fired when a VoltageRatioInput channel with onVoltageRatioChangeHandler registered meets DataInterval and ChangeTrigger criteria
*
* @param self The VoltageRatioInput channel that fired the VoltageRatioChange event
* @param voltageRatio The reported voltage ratio from the VoltageRatioInput channel
"""

test = []
test2 = []
def onVoltageRatioChangeHandler(self, voltageRatio):

    #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
    #www.phidgets.com/docs/Using_Multiple_Phidgets for information

    # print("[VoltageRatio Event] -> Voltage Ratio: " + str(voltageRatio))
    # # self.chanlist.clear()
    # # self.chanlist.append(voltageRatio)
    # # if self not in test:
    # #     test.append(self)
    # #print(self.chanlist)
    # #print(test)

    # test2.append(voltageRatio)
    # #print(test2)
    # if len(test2) % 4 == 0:
    #     print('list is div by 4')
    #     n0 = test2[len(test2)-1]
    #     n1 = test2[len(test2)-2]
    #     nsum = n0 + n1
    #     print('n0 = ' + str(n0) + '  n1 = ' + str(n1) + '  SUM OF VALS = ' + str(nsum))
    # else:
    #     nsum = 0
    # if len(test2) > 3:
    #     del test2[:]
    #     # test2.clear()
    # self.nsum = nsum
    # self.vrlist = []
    # self.vrlist.append(voltageRatio)
    self.vrval = voltageRatio

"""
* Outputs the VoltageRatioInput's most recently reported sensor value.
* Fired when a VoltageRatioInput channel with onSensorChangeHandler registered meets DataInterval and ChangeTrigger criteria
*
* @param self The VoltageRatioInput channel that fired the SensorChange event
* @param sensorValue The reported sensor value from the VoltageRatioInput channel
"""
def onSensorChangeHandler(self, sensorValue, sensorUnit):

    #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
    #www.phidgets.com/docs/Using_Multiple_Phidgets for information

    print("[Sensor Event] -> Sensor Value: " + str(sensorValue) + sensorUnit.symbol)


"""
* Prints descriptions of how events related to this class work
"""
def PrintEventDescriptions():

    print("\n--------------------\n"
        "\n  | Voltage Ratio change events will call their associated function every time new voltage ratio data is received from the device.\n"
        "  | The rate of these events can be set by adjusting the DataInterval for the channel.\n")

    print(
        "\n  | Sensor change events contain the most recent sensor value received from the device.\n"
        "  | Sensor change events will occur instead of Voltage Ratio change events if the SensorType is changed from the default.\n"
        "  | Press ENTER once you have read this message.")
    readin = sys.stdin.readline(1)

    print("\n--------------------")

