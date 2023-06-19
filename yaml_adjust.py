from ruamel.yaml import YAML

if __name__ == "__main__":
    
    yaml = YAML()
    
    with open ("/home/yueju/yue.pm_robot/match_pm_robot/pm_robot_description/calibration_config/pm_robot_joint_calibration.yaml"
            , "r") as file:
        joint_calibration = yaml.load(file)
        
        joint_calibration['PM_Robot_Tool_TCP_Joint']['x_offset'] = 10
        
    with open('/home/yueju/juyue/asd.yaml','w') as new_file:
        yaml.dump(joint_calibration, new_file)
