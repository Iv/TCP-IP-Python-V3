from dobot_api import DobotApiDashboard, DobotApi, DobotApiMove

PARAMS=0
def connect_robot():
    try:
        ip = "192.168.5.1"
        dashboard_p = 29999
        move_p = 30003
        feed_p = 30004
        print("Connecting...")
        dashboard = DobotApiDashboard(ip, dashboard_p)
        move = DobotApiMove(ip, move_p)
        feed = DobotApi(ip, feed_p)
        print(">.<Connection successful>!<")
        return dashboard, move, feed
    except Exception as e:
        print(":(Connection failed:(")
        raise e

if __name__ == '__main__':
    dashboard, move, feed = connect_robot()
   
    """
    ************************************
    ************************************
        if PARAMS  Conditional compilation: whether the instruction has parameters
            0  Instruction without parameters
            1  Instruction with parameters
            
        Examples include the following instructions:
            EnableRobot
            DisableRobot
            DO
            AccJ
            SetArmOrientation
            RunScript
            GetTraceStartPose
            PositiveSolution
            InverseSolution
            GetPose
            ModbusCreate
            GetHoldRegs
            DOGroup
            SetCollideDrag
            SetTerminal485
            MovL
            MovLIO
            MoveJog
            StartTrace
            RelMovJUser
            Circle3
    """
    
    """
    ************************************
    ************************************
     * Command: EnableRobot
     * Function: Enable the robot
    """
    if PARAMS:
      dashboard.EnableRobot()    # No parameters
    else:
       load=0.1
       centerX=0.1
       centerY=0.1
       centerZ=0.1
       dashboard.EnableRobot(load)    # One parameter
       
       dashboard.EnableRobot(load, centerX, centerY, centerZ)    # Four parameters
  
    """
    ************************************
    ************************************
     * Command: DisableRobot
     * Function: Disable the robot
    """
    dashboard.DisableRobot()    # No parameters
     
     
    """
    ************************************
    ************************************
     * Command: DO
     * Function: Set digital output port status (queue command)
    """
    index=1
    status=1
    dashboard.DO(index,status)  
     
     
    """
     *******************************
     *******************************
     * Command: AccJ
     * Function: Set joint acceleration ratio. This command is only valid for MovJ, MovJIO, MovJR, JointMovJ commands.
    """
    index=1
    dashboard.AccJ(index)  
     
     
    """
     ******************************
     ******************************
     * Command: SetArmOrientation
     * Function: Set hand orientation command.
    """
    if PARAMS:
        LorR=1
        dashboard.SetArmOrientation(LorR)    # 1 parameter
    else:
        LorR=1
        UorD=1
        ForN=1
        Config=1
        dashboard.SetArmOrientation(LorR, UorD, ForN, Config)    # 4 parameters
    
    
    """
    ************************************
    ************************************
     * Command: RunScript
     * Function: Run lua script.
    """
    name="luaname"
    dashboard.RunScript(name)  
     
     
    """
    ************************************
    ************************************
     * Command: GetTraceStartPose
     * Function: Get the first point in trajectory fitting.
    """
    traceName="name"
    dashboard.GetTraceStartPose(traceName)  
     
     
     
    """
    ************************************
    ************************************
     * Command: PositiveSolution
     * Function: Positive solution (given the angles of each joint of the robot, calculate the spatial position of the robot end).
    """
    J1=0.1
    J2=0.1
    J3=0.1
    J4=0.1
    J5=0.1
    J6=0.1
    User=1
    Tool=1
    dashboard.PositiveSolution(J1, J2, J3, J4,J5,J6,User, Tool)    

     
    """
    ************************************
    ************************************
     * Command: InverseSolution
     * Function: Inverse solution (given the position and posture of the robot end, calculate the angle values of each joint of the robot).
    """  
    if PARAMS:
        J1=0.1
        J2=0.1
        J3=0.1
        J4=0.1
        J5=0.1
        J6=0.1
        User=1
        Tool=1
        dashboard.InverseSolution(J1, J2, J3, J4,J5,J6,User, Tool)    # 1 parameter
    else:
        J1=0.1
        J2=0.1
        J3=0.1
        J4=0.1
        J5=0.1
        J6=0.1        
        User=1
        Tool=1
        isJointNear=1
        JointNear="JointNear"
        dashboard.InverseSolution(J1, J2, J3, J4,J5,J6,User, Tool,isJointNear, JointNear)  
    
  
    """
    ************************************
    ************************************
     * Command: GetPose
     * Function: Get the real-time pose of the robot arm in the Cartesian coordinate system
    """  
    if PARAMS:
        dashboard.GetPose()    
    else:
        User=1
        Tool=1
        dashboard.GetPose(User, Tool)  
    
    
    """
    ************************************
    ************************************
     * Command: ModbusCreate
     * Function: Create Modbus master
    """
    if PARAMS:
        ip="192.168.1.6"
        port=29999
        slave_id=1
        dashboard.ModbusCreate(ip, port, slave_id)    # 3 parameters
    else:
        ip="192.168.1.6"
        port=29999
        slave_id=1
        isRTU=1
        dashboard.ModbusCreate(ip, port, slave_id, isRTU)    # 4 parameters
     
     
    """
    ************************************
    ************************************
     * Command: GetHoldRegs
     * Function: Read holding registers.
       """
    if PARAMS:
        index=1
        addr=1
        count=1
        dashboard.GetHoldRegs(index, addr, count)    # 3 parameters
    else:
        index=1
        addr=1
        count=1
        valType="valType"
        dashboard.GetHoldRegs(index, addr, count, valType)    # 4 parameters    
     
    """
    ************************************
    ************************************
     * Command: DOGroup
     * Function: Set output group port status (Maximum 64 parameters supported)
    """
    if PARAMS:
        index=1
        value=1
        dashboard.DOGroup(index, value)    # 2 parameters
    else:
        index=1
        value=1
        index2=1
        value2=1
        index32=1
        value32=1
        dashboard.DOGroup(index, value, index2, value2, index32, value32)    # 64 parameters (parameters omitted)
     
     
    """
    ************************************
    ************************************
     * Command: SetCollideDrag
     * Function: Set whether to force enter drag mode (can enter drag mode even in error state)
    """
    status=1
    dashboard.SetCollideDrag(status)

    """
    ************************************
    ************************************
     * Command: SetTerminal485
     * Function: Set terminal 485 parameters
    """
    baudRate=1
    dataLen=1
    parityBit="parityBit"
    stopBit=1
    dashboard.SetTerminal485(baudRate, dataLen, parityBit, stopBit)
 
     
    """
    ************************************
    ************************************
     * Command: MovL
     * Function: Point-to-point motion, target position is Cartesian position
    """
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        move.MovL(x, y, z, rx, ry, rz)    # No optional parameters
    else:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        userparam="User=1"
        toolparam="Tool=1"
        speedlparam="SpeedL=1"
        acclparam="AccL=1"
        cpparam="CP=1" 
        move.MovL(x, y, z, rx, ry, rz,userparam)    # Set user, optional parameters order is interchangeable
        move.MovL(x, y, z, rx, ry, rz,userparam, toolparam)    # Set user tool
        move.MovL(x, y, z, rx, ry, rz,userparam, toolparam, speedlparam,)    # Set user tool speedl 
        move.MovL(x, y, z, rx, ry, rz,userparam, toolparam, speedlparam, acclparam)    # Set user tool speedl accl
        move.MovL(x, y, z, rx, ry, rz,userparam, toolparam, speedlparam, acclparam, cpparam)    # Set user tool speedl accl cp
     
     
    """
    ************************************
    ************************************
    * Command: Arc
    * Function: Move from the current position to the target position in Cartesian coordinate system in arc interpolation mode.
 	This command needs to be combined with other motion commands to determine the starting point of the arc.
    """
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        x2=1.0
        y2=1.0
        z2=1.0
        rx2=1.0
        ry2=1.0
        rz2=1.0
        move.Arc(x, y, z, rx, ry, rz,x2, y2, z2,rx2, ry2, rz2)    # No optional parameters
    else:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        x2=1.0
        y2=1.0
        z2=1.0
        rx2=1.0
        ry2=1.0
        rz2=1.0
        userparam="User=1"
        toolparam="Tool=1"
        speedlparam="SpeedL=1"
        acclparam="AccL=1"
        cpparam="CP=1" 
        move.Arc(x, y, z, rx, ry, rz,x2, y2, z2,rx2, ry2, rz2,cpparam,userparam,speedlparam, toolparam, speedlparam, acclparam)    # user tool order is not fixed and interchangeable
 
 
    """
    ************************************
    ************************************
     * Command: MovLIO
     * Function: Set digital output port status in parallel during linear motion, target position is Cartesian position.
    """
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        Mode=1
        Distance=1
        Index=1
        Status=1
        move.MovLIO(x, y, z, rx,ry,rz, Mode, Distance, Index, Status)    # No optional parameters
    else:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        Mode=1
        Distance=1
        Index=1
        Status=1
        userparam="User=1"
        toolparam="Tool=1"
        speedlparam="SpeedL=1"
        acclparam="AccL=1"
        cpparam="CP=1" 
        move.MovLIO(x, y, z, rx,ry,rz,Mode, Distance, Index, Status,cpparam,userparam,speedlparam, toolparam, speedlparam, acclparam)    # user tool order is not fixed and interchangeable    
     
    """
    ************************************
    ************************************
     * Command: MoveJog
     * Function: Jog motion, non-fixed distance motion
    """
    if PARAMS:
        axisID=""
        move.MoveJog(axisID)           
    else:
        axisID="J1+"
        CoordType="CoordType=1"
        userparam="User=0"
        toolparam="Tool=0"
        move.MoveJog(axisID, CoordType, userparam, toolparam)    

    ## Send MoveJog() stop command to control the robot to stop moving
    move.MoveJog()
    
    
    """
    ************************************
    ************************************
     * Command: StartTrace
     * Function: Trajectory fitting. (Trajectory file Cartesian points)
    """
    traceName="traceName"
    move.StartTrace(traceName)           
 
 
    """
    ************************************
    ************************************
     * Command: RelMovJUser
     * Function: Relative motion command along the user coordinate system, end motion mode is joint motion.
    """
    x=1.0
    y=1.0
    z=1.0
    rx=1.0
    ry=1.0
    rz=1.0
    User=1
    move.RelMovJUser(x,y,z,rx,ry,rz,traceName)      
    

    """
    ************************************
    ************************************
     * Command: Circle3
     * Function: Full circle motion, only effective for Cartesian points.
    """   
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        rx=1.0
        ry=1.0
        rz=1.0
        count=1
        move.Circle3(x, y, z, rx,ry,rz,count)           
    else:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        count=1
        userparam="User=0"
        toolparam="Tool=0"
        speedlparam="SpeedL=R"
        acclparam="AccL=R"
        move.Circle3(x, y, z, rx,ry,rz,count, userparam, toolparam, speedlparam, acclparam)       