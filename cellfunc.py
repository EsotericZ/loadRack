
"""
* Creates, configures, and opens a VoltageRatioInput channel.
* Displays Voltage Ratio events for 10 seconds
* Closes out VoltageRatioInput channel
*
* @return 0 if the program exits successfully, 1 if it exits with errors.
"""
from liblr import VoltageRatioInput, PhidgetException, onAttachHandler, onDetachHandler
from liblr import onErrorHandler, onVoltageRatioChangeHandler
from liblr import onSensorChangeHandler, PrintEventDescriptions
import sys
import time

def getvr(sampletime=1):
    try:
        """
        * Allocate a new Phidget Channel object
        """
        try:
            # RACK 01
            ch0 = VoltageRatioInput()
            ch1 = VoltageRatioInput()
            ch2 = VoltageRatioInput()
            ch3 = VoltageRatioInput()

            # RACK 02
            ch4 = VoltageRatioInput()
            ch5 = VoltageRatioInput()
            ch6 = VoltageRatioInput()
            ch7 = VoltageRatioInput()

            # RACK 03
            ch8 = VoltageRatioInput()
            ch9 = VoltageRatioInput()
            ch10 = VoltageRatioInput()
            ch11 = VoltageRatioInput()

            # RACK 19
            ch12 = VoltageRatioInput()
            ch13 = VoltageRatioInput()
            ch14 = VoltageRatioInput()
            ch15 = VoltageRatioInput()

            # RACK 20
            ch16 = VoltageRatioInput()
            ch17 = VoltageRatioInput()
            ch18 = VoltageRatioInput()
            ch19 = VoltageRatioInput()
        except PhidgetException as e:
            sys.stderr.write("Runtime Error -> Creating VoltageRatioInput: \n\t")
            DisplayError(e)
            raise
        except RuntimeError as e:
            sys.stderr.write("Runtime Error -> Creating VoltageRatioInput: \n\t" + e)
            raise

        """
        * Set matching parameters to specify which channel to open
        """

        # SET SERIAL NUMBERS CJ

        # RACK 01
        ch0.setDeviceSerialNumber(544784)
        ch0.setHubPort(0)
        ch0.setChannel(0)
        ch1.setDeviceSerialNumber(544784)
        ch1.setHubPort(0)
        ch1.setChannel(1)
        ch2.setDeviceSerialNumber(544784)
        ch2.setHubPort(0)
        ch2.setChannel(2)
        ch3.setDeviceSerialNumber(544784)
        ch3.setHubPort(0)
        ch3.setChannel(3)

        # RACK 02
        ch4.setDeviceSerialNumber(544947)
        ch4.setHubPort(0)
        ch4.setChannel(0)
        ch5.setDeviceSerialNumber(544947)
        ch5.setHubPort(0)
        ch5.setChannel(1)
        ch6.setDeviceSerialNumber(544947)
        ch6.setHubPort(0)
        ch6.setChannel(2)
        ch7.setDeviceSerialNumber(544947)
        ch7.setHubPort(0)
        ch7.setChannel(3)

        # RACK 03
        ch8.setDeviceSerialNumber(588672)
        ch8.setHubPort(0)
        ch8.setChannel(0)
        ch9.setDeviceSerialNumber(588672)
        ch9.setHubPort(0)
        ch9.setChannel(1)
        ch10.setDeviceSerialNumber(588672)
        ch10.setHubPort(0)
        ch10.setChannel(2)
        ch11.setDeviceSerialNumber(588672)
        ch11.setHubPort(0)
        ch11.setChannel(3)

        # RACK 19
        ch12.setDeviceSerialNumber(583165)
        ch12.setHubPort(0)
        ch12.setChannel(0)
        ch13.setDeviceSerialNumber(583165)
        ch13.setHubPort(0)
        ch13.setChannel(1)
        ch14.setDeviceSerialNumber(583165)
        ch14.setHubPort(0)
        ch14.setChannel(2)
        ch15.setDeviceSerialNumber(583165)
        ch15.setHubPort(0)
        ch15.setChannel(3)

        # RACK 20
        ch16.setDeviceSerialNumber(533467)
        ch16.setHubPort(0)
        ch16.setChannel(0)
        ch17.setDeviceSerialNumber(533467)
        ch17.setHubPort(0)
        ch17.setChannel(1)
        ch18.setDeviceSerialNumber(533467)
        ch18.setHubPort(0)
        ch18.setChannel(2)
        ch19.setDeviceSerialNumber(533467)
        ch19.setHubPort(0)
        ch19.setChannel(3)

        """
        * Add event handlers before calling open so that no events are missed.
        """

        # ch = [VoltageRatioInput() for i in range(0,4)]

        # for i in range(0,4):
        #     ch[i].setOnAttachHandler(onAttachHandler)
        #     ch[i].setOnDetachHandler(onDetachHandler)
        #     ch[i].setOnErrorHandler(onErrorHandler)
        #     ch[i].setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        #     ch[i].setOnSensorChangeHandler(onSensorChangeHandler)

        # RACK 01
        ch0.setOnAttachHandler(onAttachHandler)
        ch1.setOnAttachHandler(onAttachHandler)
        ch2.setOnAttachHandler(onAttachHandler)
        ch3.setOnAttachHandler(onAttachHandler)
        ch0.setOnDetachHandler(onDetachHandler)
        ch1.setOnDetachHandler(onDetachHandler)
        ch2.setOnDetachHandler(onDetachHandler)
        ch3.setOnDetachHandler(onDetachHandler)
        ch0.setOnErrorHandler(onErrorHandler)
        ch1.setOnErrorHandler(onErrorHandler)
        ch2.setOnErrorHandler(onErrorHandler)
        ch3.setOnErrorHandler(onErrorHandler)
        ch0.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch1.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch2.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch3.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch0.setOnSensorChangeHandler(onSensorChangeHandler)
        ch1.setOnSensorChangeHandler(onSensorChangeHandler)
        ch2.setOnSensorChangeHandler(onSensorChangeHandler)
        ch3.setOnSensorChangeHandler(onSensorChangeHandler)

        # RACK 02
        ch4.setOnAttachHandler(onAttachHandler)
        ch5.setOnAttachHandler(onAttachHandler)
        ch6.setOnAttachHandler(onAttachHandler)
        ch7.setOnAttachHandler(onAttachHandler)
        ch4.setOnDetachHandler(onDetachHandler)
        ch5.setOnDetachHandler(onDetachHandler)
        ch6.setOnDetachHandler(onDetachHandler)
        ch7.setOnDetachHandler(onDetachHandler)
        ch4.setOnErrorHandler(onErrorHandler)
        ch5.setOnErrorHandler(onErrorHandler)
        ch6.setOnErrorHandler(onErrorHandler)
        ch7.setOnErrorHandler(onErrorHandler)
        ch4.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch5.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch6.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch7.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch4.setOnSensorChangeHandler(onSensorChangeHandler)
        ch5.setOnSensorChangeHandler(onSensorChangeHandler)
        ch6.setOnSensorChangeHandler(onSensorChangeHandler)
        ch7.setOnSensorChangeHandler(onSensorChangeHandler)

        # RACK 03
        ch8.setOnAttachHandler(onAttachHandler)
        ch9.setOnAttachHandler(onAttachHandler)
        ch10.setOnAttachHandler(onAttachHandler)
        ch11.setOnAttachHandler(onAttachHandler)
        ch8.setOnDetachHandler(onDetachHandler)
        ch9.setOnDetachHandler(onDetachHandler)
        ch10.setOnDetachHandler(onDetachHandler)
        ch11.setOnDetachHandler(onDetachHandler)
        ch8.setOnErrorHandler(onErrorHandler)
        ch9.setOnErrorHandler(onErrorHandler)
        ch10.setOnErrorHandler(onErrorHandler)
        ch11.setOnErrorHandler(onErrorHandler)
        ch8.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch9.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch10.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch11.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch8.setOnSensorChangeHandler(onSensorChangeHandler)
        ch9.setOnSensorChangeHandler(onSensorChangeHandler)
        ch10.setOnSensorChangeHandler(onSensorChangeHandler)
        ch11.setOnSensorChangeHandler(onSensorChangeHandler)

        # RACK 19
        ch12.setOnAttachHandler(onAttachHandler)
        ch13.setOnAttachHandler(onAttachHandler)
        ch14.setOnAttachHandler(onAttachHandler)
        ch15.setOnAttachHandler(onAttachHandler)
        ch12.setOnDetachHandler(onDetachHandler)
        ch13.setOnDetachHandler(onDetachHandler)
        ch14.setOnDetachHandler(onDetachHandler)
        ch15.setOnDetachHandler(onDetachHandler)
        ch12.setOnErrorHandler(onErrorHandler)
        ch13.setOnErrorHandler(onErrorHandler)
        ch14.setOnErrorHandler(onErrorHandler)
        ch15.setOnErrorHandler(onErrorHandler)
        ch12.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch13.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch14.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch15.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch12.setOnSensorChangeHandler(onSensorChangeHandler)
        ch13.setOnSensorChangeHandler(onSensorChangeHandler)
        ch14.setOnSensorChangeHandler(onSensorChangeHandler)
        ch15.setOnSensorChangeHandler(onSensorChangeHandler)

        # RACK 20
        ch16.setOnAttachHandler(onAttachHandler)
        ch17.setOnAttachHandler(onAttachHandler)
        ch18.setOnAttachHandler(onAttachHandler)
        ch19.setOnAttachHandler(onAttachHandler)
        ch16.setOnDetachHandler(onDetachHandler)
        ch17.setOnDetachHandler(onDetachHandler)
        ch18.setOnDetachHandler(onDetachHandler)
        ch19.setOnDetachHandler(onDetachHandler)
        ch16.setOnErrorHandler(onErrorHandler)
        ch17.setOnErrorHandler(onErrorHandler)
        ch18.setOnErrorHandler(onErrorHandler)
        ch19.setOnErrorHandler(onErrorHandler)
        ch16.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch17.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch18.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch19.setOnVoltageRatioChangeHandler(onVoltageRatioChangeHandler)
        ch16.setOnSensorChangeHandler(onSensorChangeHandler)
        ch17.setOnSensorChangeHandler(onSensorChangeHandler)
        ch18.setOnSensorChangeHandler(onSensorChangeHandler)
        ch19.setOnSensorChangeHandler(onSensorChangeHandler)

        """
        * Open the channel with a timeout
        """

        try:
            # RACK 01
            ch0.openWaitForAttachment(5000)
            ch1.openWaitForAttachment(5000)
            ch2.openWaitForAttachment(5000)
            ch3.openWaitForAttachment(5000)

            # RACK 02
            ch4.openWaitForAttachment(5000)
            ch5.openWaitForAttachment(5000)
            ch6.openWaitForAttachment(5000)
            ch7.openWaitForAttachment(5000)

            # RACK 03
            ch8.openWaitForAttachment(5000)
            ch9.openWaitForAttachment(5000)
            ch10.openWaitForAttachment(5000)
            ch11.openWaitForAttachment(5000)

            # RACK 19
            ch12.openWaitForAttachment(5000)
            ch13.openWaitForAttachment(5000)
            ch14.openWaitForAttachment(5000)
            ch15.openWaitForAttachment(5000)

            # RACK 20
            ch16.openWaitForAttachment(5000)
            ch17.openWaitForAttachment(5000)
            ch18.openWaitForAttachment(5000)
            ch19.openWaitForAttachment(5000)
        except PhidgetException as e:
            PrintOpenErrorMessage(e, ch)
            raise EndProgramSignal("Program Terminated: Open Failed")

        # print("Sampling data for 10 seconds...")

        # print("You can do stuff with your Phidgets here and/or in the event handlers.")

        #This controls how long the program runs CJ
        time.sleep(3)

        """
        * Perform clean up and exit
        """

        # RACK 01
        ch0.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch1.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch2.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch3.setOnVoltageRatioChangeHandler(None) # Get voltage info here

        # RACK 02
        ch4.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch5.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch6.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch7.setOnVoltageRatioChangeHandler(None) # Get voltage info here

        # RACK 03
        ch8.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch9.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch10.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch11.setOnVoltageRatioChangeHandler(None) # Get voltage info here

        # RACK 19
        ch12.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch13.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch14.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch15.setOnVoltageRatioChangeHandler(None) # Get voltage info here

        # RACK 20
        ch16.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch17.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch18.setOnVoltageRatioChangeHandler(None) # Get voltage info here
        ch19.setOnVoltageRatioChangeHandler(None) # Get voltage info here

        ch0.close()
        ch1.close()
        ch2.close()
        ch3.close()

        ch4.close()
        ch5.close()
        ch6.close()
        ch7.close()

        ch8.close()
        ch9.close()
        ch10.close()
        ch11.close()

        ch12.close()
        ch13.close()
        ch14.close()
        ch15.close()

        ch16.close()
        ch17.close()
        ch18.close()
        ch19.close()

        # print('v0: {}'.format(ch0.vrval))
        # print('v1: {}'.format(ch1.vrval))
        # return ch0.vrval,ch1.vrval,ch2.vrval,ch3.vrval, ch4.vrval, ch5.vrval, ch6.vrval, ch7.vrval
        # return ch8.vrval, ch9.vrval, ch10.vrval, ch11.vrval, ch4.vrval, ch5.vrval, ch6.vrval, ch7.vrval

        r1 = [ch0.vrval, ch1.vrval, ch2.vrval, ch3.vrval]
        r2 = [ch4.vrval, ch5.vrval, ch6.vrval, ch7.vrval]
        r3 = [ch8.vrval, ch9.vrval, ch10.vrval, ch11.vrval]
        r19 = [ch12.vrval, ch13.vrval, ch14.vrval, ch15.vrval]
        r20 = [ch16.vrval, ch17.vrval, ch18.vrval, ch19.vrval]
        return r1, r2, r3, r19, r20
        # print('This is r1 ', r1)
        # return r1

    except PhidgetException as e:
        sys.stderr.write("\nExiting with error(s)...")
        DisplayError(e)
        traceback.print_exc()
        print("Cleaning up...")
        ch0.setOnVoltageRatioChangeHandler(None)
        ch0.setOnSensorChangeHandler(None)
        ch0.close()
        ch1.setOnVoltageRatioChangeHandler(None)
        ch1.setOnSensorChangeHandler(None)
        ch1.close()
        ch2.setOnVoltageRatioChangeHandler(None)
        ch2.setOnSensorChangeHandler(None)
        ch2.close()
        ch3.setOnVoltageRatioChangeHandler(None)
        ch3.setOnSensorChangeHandler(None)
        ch3.close()

        ch4.setOnVoltageRatioChangeHandler(None)
        ch4.setOnSensorChangeHandler(None)
        ch4.close()
        ch5.setOnVoltageRatioChangeHandler(None)
        ch5.setOnSensorChangeHandler(None)
        ch5.close()
        ch6.setOnVoltageRatioChangeHandler(None)
        ch6.setOnSensorChangeHandler(None)
        ch6.close()
        ch7.setOnVoltageRatioChangeHandler(None)
        ch7.setOnSensorChangeHandler(None)
        ch7.close()

        ch8.setOnVoltageRatioChangeHandler(None)
        ch8.setOnSensorChangeHandler(None)
        ch8.close()
        ch9.setOnVoltageRatioChangeHandler(None)
        ch9.setOnSensorChangeHandler(None)
        ch9.close()
        ch10.setOnVoltageRatioChangeHandler(None)
        ch10.setOnSensorChangeHandler(None)
        ch10.close()
        ch11.setOnVoltageRatioChangeHandler(None)
        ch11.setOnSensorChangeHandler(None)
        ch11.close()

        ch12.setOnVoltageRatioChangeHandler(None)
        ch12.setOnSensorChangeHandler(None)
        ch12.close()
        ch13.setOnVoltageRatioChangeHandler(None)
        ch13.setOnSensorChangeHandler(None)
        ch13.close()
        ch14.setOnVoltageRatioChangeHandler(None)
        ch14.setOnSensorChangeHandler(None)
        ch14.close()
        ch15.setOnVoltageRatioChangeHandler(None)
        ch15.setOnSensorChangeHandler(None)
        ch15.close()

        ch16.setOnVoltageRatioChangeHandler(None)
        ch16.setOnSensorChangeHandler(None)
        ch16.close()
        ch17.setOnVoltageRatioChangeHandler(None)
        ch17.setOnSensorChangeHandler(None)
        ch17.close()
        ch18.setOnVoltageRatioChangeHandler(None)
        ch18.setOnSensorChangeHandler(None)
        ch18.close()
        ch19.setOnVoltageRatioChangeHandler(None)
        ch19.setOnSensorChangeHandler(None)
        ch19.close()
        # return 1
    except EndProgramSignal as e:
        print(e)
        print("Cleaning up...")
        ch0.setOnVoltageRatioChangeHandler(None)
        ch0.setOnSensorChangeHandler(None)
        ch0.close()
        ch1.setOnVoltageRatioChangeHandler(None)
        ch1.setOnSensorChangeHandler(None)
        ch1.close()
        ch2.setOnVoltageRatioChangeHandler(None)
        ch2.setOnSensorChangeHandler(None)
        ch2.close()
        ch3.setOnVoltageRatioChangeHandler(None)
        ch3.setOnSensorChangeHandler(None)
        ch3.close()

        ch4.setOnVoltageRatioChangeHandler(None)
        ch4.setOnSensorChangeHandler(None)
        ch4.close()
        ch5.setOnVoltageRatioChangeHandler(None)
        ch5.setOnSensorChangeHandler(None)
        ch5.close()
        ch6.setOnVoltageRatioChangeHandler(None)
        ch6.setOnSensorChangeHandler(None)
        ch6.close()
        ch7.setOnVoltageRatioChangeHandler(None)
        ch7.setOnSensorChangeHandler(None)
        ch7.close()

        ch8.setOnVoltageRatioChangeHandler(None)
        ch8.setOnSensorChangeHandler(None)
        ch8.close()
        ch9.setOnVoltageRatioChangeHandler(None)
        ch9.setOnSensorChangeHandler(None)
        ch9.close()
        ch10.setOnVoltageRatioChangeHandler(None)
        ch10.setOnSensorChangeHandler(None)
        ch10.close()
        ch11.setOnVoltageRatioChangeHandler(None)
        ch11.setOnSensorChangeHandler(None)
        ch11.close()

        ch12.setOnVoltageRatioChangeHandler(None)
        ch12.setOnSensorChangeHandler(None)
        ch12.close()
        ch13.setOnVoltageRatioChangeHandler(None)
        ch13.setOnSensorChangeHandler(None)
        ch13.close()
        ch14.setOnVoltageRatioChangeHandler(None)
        ch14.setOnSensorChangeHandler(None)
        ch14.close()
        ch15.setOnVoltageRatioChangeHandler(None)
        ch15.setOnSensorChangeHandler(None)
        ch15.close()

        ch16.setOnVoltageRatioChangeHandler(None)
        ch16.setOnSensorChangeHandler(None)
        ch16.close()
        ch17.setOnVoltageRatioChangeHandler(None)
        ch17.setOnSensorChangeHandler(None)
        ch17.close()
        ch18.setOnVoltageRatioChangeHandler(None)
        ch18.setOnSensorChangeHandler(None)
        ch18.close()
        ch19.setOnVoltageRatioChangeHandler(None)
        ch19.setOnSensorChangeHandler(None)
        ch19.close()
        # return 1
