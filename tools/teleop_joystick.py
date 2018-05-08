import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# cmd_vel_pub = None
tw = None

def joy_cb(msg):
    # global cmd_vel_pub
    global tw

    # For my unknown branch joystick:
    # x = msg.axes[3]
    # y = msg.axes[2]
    # z = msg.axes[0]

    # For xbox360 joystick:
    x = msg.axes[4]
    y = msg.axes[3]
    z = msg.axes[0]

    tw = Twist()
    tw.linear.x = x
    tw.linear.y = y
    tw.angular.z = z
    # cmd_vel_pub.publish(tw)

def main():
    # global cmd_vel_pub
    global tw
    rospy.init_node('key_op')
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/joy', Joy, joy_cb)
    # rospy.spin()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if tw != None:
            cmd_vel_pub.publish(tw)
        rate.sleep()

if __name__ == '__main__':
    main()
