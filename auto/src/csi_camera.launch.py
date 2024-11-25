from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gscam',
            executable='gscam_node',
            name='csi_cam_0',
            output='screen',
            parameters=[{
                'camera_name': 'csi_cam_0',
                'camera_info_url': 'file:///home/jetson/.ros/camera_info/csi_cam_0.yaml',
                'sync_sink': False,
                'gscam_config': 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv flip-method=0 ! videoconvert'
            }],
            remappings=[
                ('camera/image_raw', 'csi_cam_0/image_raw'),
                ('/set_camera_info', 'csi_cam_0/set_camera_info'),
            ]
        )
    ])
