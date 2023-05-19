#!/usr/bin/env python3

import rospy
import smach
import smach_ros

# define state SOUND1
class Sound1(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['sound1_counter_in'],
                             output_keys['sound1_counter_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state SOUND1')
        rospy.sleep(3)
        if userdata.sound1_counter_in < 3:
            userdata.sound1_counter_out = userdata.sound1_counter_in + 1
            return 'outcome1'
        else:
            return 'outcome2'

# define state Failed1
class Failed1(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['failed1_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state FAILED1')
        rospy.loginfo('Counter = %f'%userdata.failed1_counter_in)
        rospy.sleep(3)
        return 'outcome2'

# define state MoveRack
class MoveRack(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['moverack_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state MOVERACK')
        rospy.loginfo('Counter = %f'%userdata.moverack_counter_in)
        rospy.sleep(3)
        return 'outcome2'
        
# define state DetectQR
class DetectQR(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['detectqr_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state DETECTQR')
        rospy.loginfo('Counter = %f'%userdata.detectqr_counter_in)
        rospy.sleep(3)
        return 'outcome2'

# define state DetectObject
class DetectObject(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['detectobject_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state DETECTOBJECT')
        rospy.loginfo('Counter = %f'%userdata.detectobject_counter_in)
        rospy.sleep(3)
        return 'outcome2'
        
# define state MoveInit
class MoveInit(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['moveinit_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state MOVEINIT')
        rospy.loginfo('Counter = %f'%userdata.moveinit_counter_in)
        rospy.sleep(3)
        return 'outcome2'

# define state Sound2
class Sound2(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['sound2_counter_in'],
                             output_keys['sound2_counter_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state SOUND2')
        rospy.sleep(3)
        if userdata.sound2_counter_in < 3:
            userdata.sound2_counter_out = userdata.sound2_counter_in + 1
            return 'outcome1'
        else:
            return 'outcome2'
            
# define state Failed2
class Failed2(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['failed2_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state FAILED2')
        rospy.loginfo('Counter = %f'%userdata.failed2_counter_in)
        rospy.sleep(3)
        return 'outcome2'

# define state Announce
class Announce(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['announce_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state Announce')
        rospy.loginfo('Counter = %f'%userdata.announce_counter_in)
        rospy.sleep(3)
        return 'outcome2'

# define state Sound3
class Sound3(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome2'],
                             input_keys=['sound3_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state Sound3')
        rospy.loginfo('Counter = %f'%userdata.sound3_counter_in)
        rospy.sleep(3)
        return 'outcome2'

# main
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['EXIT'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('SOUND1', Foo(), 
                               transitions={'outcome1':'FAILED1', 
                                            'outcome2':'MOVERACK'},
                               remapping={'sound1_counter_in':'sm_counter',
                                          'sound1_counter_out':'sm_counter'})
        smach.StateMachine.add('FAILED1', Bar(), 
                               transitions={'outcome2':'SOUND1'},
                               remapping={'failed1_countter_in':'sm_counter'})
        smach.StateMachine.add('MOVERACK', Bar(), 
                               transitions={'outcome2':'DETECTQR'},
                               remapping={'moverack_countter_in':'sm_counter'})
        smach.StateMachine.add('DETECTQR', Bar(), 
                               transitions={'outcome2':'DETECTOBJECT'},
                               remapping={'detectqr_countter_in':'sm_counter'})
        smach.StateMachine.add('DETECTOBJECT', Bar(), 
                               transitions={'outcome2':'MOVEINIT'},
                               remapping={'detectobject_countter_in':'sm_counter'})
        smach.StateMachine.add('SOUND2', Foo(), 
                               transitions={'outcome1':'FAILED2', 
                                            'outcome2':'ANNOUNCE'},
                               remapping={'sound2_counter_in':'sm_counter',
                                          'sound2_counter_out':'sm_counter'})
        smach.StateMachine.add('FAILED2', Bar(), 
                               transitions={'outcome2':'SOUND2'},
                               remapping={'failed2_countter_in':'sm_counter'})
        smach.StateMachine.add('ANNOUNCE', Bar(), 
                               transitions={'outcome2':'ANNOUNCE'},
                               remapping={'announce_countter_in':'sm_counter'})
        smach.StateMachine.add('SOUND3', Bar(), 
                               transitions={'outcome2':'SOUND3'},
                               remapping={'sound3_countter_in':'sm_counter'})

    # Execute SMACH plan
    sis = smach_ros.IntrospectionServer("sm_server", sm, "/ROOT")
    sis.start()
    outcome = sm.execute()
    sis.stop()

if __name__ == '__main__':
    main()'
