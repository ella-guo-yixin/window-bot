from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
import rclpy
from geometry_msgs.msg import Twist
import threading

threading.Thread(target=lambda: rclpy.init()).start()
app = Flask(__name__)

cmd_vel_publisher = self.create_publisher(String, "topic", 10)


@app.route("/", methods=["POST", "GET"])
def AR():
    if request.method == "POST":

        """
        print(request.form)

        msg = Twist()

        if "forward_button" in request.form.keys():
            msg.linear.x = 0.1
        if "left_button" in reuqest.form.keys():
            msg.angular.z = -0.1
        if "right_button" in request.form.keys():
            msg.angular.z = 0.1

        cmd_vel_publisher.publish(msg)
        """

        msg = String("Test")
        cmd_vel_publisher.publish(msg)

    elif request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
