## Roll:

The roll control conforms to the response curve of a real drone. Since the timeline recorded in the experiment starts from the right side, it only needs to be reversed:

| Real-world drone roll attitude response curve                     | Real-world drone roll attitude response curve (reversed)       | Unity drone roll attitude response curve                         |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| ![1742808270781](image/BunnyChenDroneFramwork/1742808270781.png)[^1] | ![1742870124904](image/BunnyChenDroneFramwork/1742870124904.png) | ![1742808300656](image/BunnyChenDroneFramwork/1742808300656.png)[^2] |

| Real-world drone yaw attitude response curve                      | Unity drone roll attitude response curve (reversed)            | Unity drone roll attitude response curve                         |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| ![1742873603848](image/BunnyChenDroneFramwork/1742873603848.png)[^3] | ![1742873821935](image/BunnyChenDroneFramwork/1742873821935.png) | ![1742873678526](image/BunnyChenDroneFramwork/1742873678526.png) |

## Power

| Relationship between battery power and response                   | Relationship between motor power and response in Unity         |
| ------------------------------------------------------------------ | -------------------------------------------------------------- |
| ![1742874136300](image/BunnyChenDroneFramwork/1742874136300.png)[^4] | ![1742873678526](image/BunnyChenDroneFramwork/1742873678526.png) |

## Altitude

![1742875740467](image/BunnyChenDroneFramwork/1742875740467.png)

[^1]: [Model-Based Optimization Approach for PID Control of Pitch&amp;ndash;Roll UAV Orientation](https://www.mdpi.com/2227-7390/11/15/3390#)
    
[^2]: [BunnyChenFramework]()
    
[^3]: [AR.Drone UAV control parameters tuning based on particle swarm optimization algorithm | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/7501380)
    
[^4]: [Model-Based Optimization Approach for PID Control of Pitch–Roll UAV Orientation](https://www.mdpi.com/2227-7390/11/15/3390)