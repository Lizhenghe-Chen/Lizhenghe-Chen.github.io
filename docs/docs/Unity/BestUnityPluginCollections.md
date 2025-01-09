# 好用的Unity插件收集

!!!abstract
      收集一些已经或者正在使用的实用（好用）的Unity插件资源

## 开发向

### HotReload

Unity 的开发难免会要不停的改代码并不断运行从而达到理想的效果，然而原生的Unity脚本编译器几乎不能实现**运行时**更改代码并实时应用新代码逻辑和变量。

HotReload 是一种技术，允许开发者在不重新启动应用程序或游戏的情况下，实时更新代码和资源。这种技术在游戏开发和软件开发中非常有用，能够显著提高开发效率。

在 Unity 中，HotReload 使得开发者可以在编辑器中修改脚本后，立即看到更改的效果，而无需停止和重新运行游戏。这对于快速迭代和调试非常重要，因为它减少了等待时间，允许开发者更快地测试和调整功能。

HotReload 的主要优点包括：

1. **提高效率**：减少了开发和测试之间的切换时间。
2. **实时反馈**：开发者可以立即看到代码更改的结果。
3. **更好的调试体验**：可以在运行时修改代码，方便调试和修复问题。

总之，HotReload 是一种提升开发体验和效率的重要工具，尤其在需要频繁修改和测试代码的场景中。

官网：[Quick Start | Hot Reload for Unity](https://hotreload.net/documentation)

资产：[Hot Reload | Edit Code Without Compiling | 实用工具 工具 | Unity Asset Store](https://assetstore.unity.com/packages/tools/utilities/hot-reload-edit-code-without-compiling-254358)

### In-game Debug Console

随时随地都能够在游戏运行时展示丰富的Log信息，在编辑器和出包后都同样适用。

官网：

资产：[In-game Debug Console | GUI 工具 | Unity Asset Store](https://assetstore.unity.com/packages/tools/gui/in-game-debug-console-68068)

### Odin Inspector and Serializer

Odin Inspector 和 Serializer 是 Unity 中用于增强和扩展编辑器功能的工具。

1. **Odin Inspector**:
   Odin Inspector 是一个 Unity 插件，用于增强 Unity 编辑器中的可视化效果和功能。它提供了大量的自定义属性和面板，让开发者可以更轻松地在 Unity 编辑器中设计和调试自己的游戏。Odin 提供了一些非常强大的特性，比如：

   - 自定义属性绘制：让开发者可以为脚本中的字段、类、枚举等添加自定义的编辑界面。
   - 增强的序列化功能：Odin 允许将 Unity 不支持的类型（如字典、集合等）序列化为 Unity 可以理解的格式。
   - 条件属性：可以根据一些条件来动态显示或隐藏属性。
   - 编辑器窗口：让开发者可以创建自己的编辑器窗口，并在其中显示数据。
2. **Odin Serializer**:
   Odin Serializer 是 Odin Inspector 的一个附加库，专门用于提供更强大和灵活的序列化功能。Unity 默认的序列化系统有一些限制，例如不支持序列化字典、接口类型或者非 Unity 类型的字段，而 Odin Serializer 可以解决这些问题。它使得在编辑器和运行时都能更方便地进行数据存储和加载。Odin Serializer 的一些特点包括：

   - 支持更广泛的数据类型，包括字典、集合和复杂的类。
   - 提供高效且可定制的序列化方式。
   - 支持跨平台和多种数据存储格式。

总之，Odin Inspector 和 Serializer 主要是用来提高开发者在 Unity 中的工作效率，尤其是在创建和调试游戏时。

官网：[Odin Inspector and Serializer | Improve your workflow in Unity](https://odininspector.com/)

资产：[Odin Inspector and Serializer | 实用工具 工具 | Unity Asset Store](https://assetstore.unity.com/packages/tools/utilities/odin-inspector-and-serializer-89041?aid=1101l4bPZ)

## 技术向

### Cinemachine

**Cinemachine** 是 Unity 中一个强大的摄像机插件，专门用于创建复杂的摄像机效果和视角控制。不需要再处理繁杂的相机脚本，能够应对绝大部分场景。它通过引入虚拟摄像机的概念，简化了开发者在 Unity 中实现高质量摄像机动画的过程，提供了简单易用的工具来控制摄像机的移动、旋转和对焦等行为。

**Cinemachine** 的一些主要功能包括：

1. **虚拟摄像机系统** ：允许开发者使用相机组件的虚拟实例，而不必直接操作实际摄像机。通过虚拟摄像机，可以灵活地设置和调整摄像机的各种参数.
2. **目标跟踪** ：能够自动跟踪和对焦游戏中的目标物体，使摄像机的运动更加平滑和自然，适用于第三人称游戏等需要跟随角色的场景.
3. **多摄像机管理** ：可以管理多个虚拟摄像机，并根据优先级和条件自动切换它们，以实现更流畅的镜头过渡和视角切换.
4. **轨道系统** ：允许开发者在3D空间中定义相机的运动路径，实现更复杂的镜头动画，如环绕角色旋转或沿着特定轨迹移动.
5. **镜头切换** ：支持创建切换镜头的区域，以便在游戏中实现不同的视角和效果，增强游戏的视觉表现力.
6. **与 Timeline 集成** ：与 Unity 的 Timeline 集成，使开发者能够在时间轴上控制和调整相机动画，方便制作剧情动画和分镜效果.
7. **渐变效果** ：通过 Impulse Listener 实现相机渐变效果，使相机对游戏中的事件有更生动的响应，如爆炸或撞击时的摄像机震动.

总的来说，**Cinemachine** 是一个功能全面且灵活的摄像机工具，适合需要精细控制摄像机视角和动画的开发者。它是做游戏摄像机控制、剧情动画或任何需要复杂摄像机效果的 Unity 项目中非常实用的插件.

官网：[Cinemachine | Unity](https://unity.com/cinemachine)

资产：[Import samples to your project | Cinemachine | 3.1.2](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/samples-import.html)

### DoTween(Pro)

**DoTween** 是 Unity 中一个非常流行且高效的动画插件，用于实现各种类型的平滑动画效果。它可以简化开发人员在 Unity 中制作动画的过程，提供了简单易用的 API 来执行物体的位置、旋转、缩放、颜色、材质等多种属性的动画。同时不局限于动画，它对连续丝滑的变量变化控制同样起到简洁高效的作用。

**DoTween Pro** 是 **DoTween** 的高级版本，除了包含免费版本的所有功能外，还增加了额外的特性和优化（针对TextMeshPro），使得动画控制更加强大和灵活。DoTween Pro 的一些主要功能包括：

1. **高级路径动画**：支持复杂的路径动画，能够使对象沿着路径进行动画移动，支持自定义路径形状和动画的插值方式。
2. **动画时间轴**：提供了更强的时间轴控制功能，支持多种动画同时进行，甚至可以让动画顺序、并行、回调等更细致地控制。
3. **性能优化**：DoTween Pro 对性能有更高的优化，适用于大规模动画需求，减少 CPU 和内存消耗。
4. **文本动画**：支持丰富的文本动画效果，可以让文字逐字显示、逐行显示等。
5. **插件扩展和支持**：提供了额外的插件和组件支持，可以与其他插件（例如，UI、材质、相机等）更好地集成。

总的来说，**DoTween Pro** 是一个功能全面且性能优化的动画工具，适合需要精细控制动画和优化性能的开发者。它是做游戏动画、UI 动画或任何需要平滑动画效果的 Unity 项目中非常实用的工具。

官网：[DOTween (HOTween v2)](https://dotween.demigiant.com/index.php)

资产：[DOTween (HOTween v2) | 动画 工具 | Unity Asset Store](https://assetstore.unity.com/packages/tools/animation/dotween-hotween-v2-27676)

### uLipSync

官网：[uLipSync でリップシンクの事前計算およびタイムライン対応をしてみた - 凹みTips](https://tips.hecomi.com/entry/2022/01/30/152519)

资产：[hecomi/uLipSync: MFCC-based LipSync plug-in for Unity using Job System and Burst Compiler](https://github.com/hecomi/uLipSync)

### Final IK

**Final IK** 是 Unity 中一个强大的逆向运动学（IK）插件，用于处理和生成复杂的角色动画。它提供了一套高效且易用的工具来实现角色骨骼系统的实时调整，特别是在需要精确控制角色肢体动作、手部位置、脚步跟随等方面。Final IK 支持许多常见的 IK 技术，可以帮助开发者快速创建自然流畅的动画，同时也让VR虚拟现实的角色形象更加生动真实。

**Final IK** 的一些关键功能包括：

1. **IK 系统**：支持全身 IK、手部 IK、脚部 IK 和面部 IK 等多种逆向运动学系统，能够让角色的肢体部位在特定位置、角度或姿势下自然移动。
2. **姿态修正**：通过 IK 技术调整角色姿势，使其自动适应环境。例如，角色可以根据地面形状调整脚步位置，避免穿模或漂浮。
3. **目标跟踪**：允许角色的身体部位（如手、脚、头）自动跟随目标对象，适用于各种场景，例如角色抓取物体、瞄准敌人等。
4. **动画与物理结合**：Final IK 还可以与 Unity 的物理系统结合，处理更加复杂的交互和动作。
5. **高度优化**：该插件经过优化，能够在不影响游戏性能的情况下运行，适合大规模使用。

总之，**Final IK** 是一个功能强大的工具，适用于需要高度控制角色动画和物理交互的游戏开发。它让开发者可以轻松实现角色与环境的互动、动态调整动画效果，从而提高游戏的沉浸感和表现力。

官网：[Home - RootMotion](http://root-motion.com/)

资产：[Final IK | 动画 工具 | Unity Asset Store](https://assetstore.unity.com/packages/tools/animation/final-ik-14290?aid=1101l4bPZ)

### TerrainToMesh

官网：

资产：[Terrain To Mesh | 地形 | Unity Asset Store](https://assetstore.unity.com/packages/tools/terrain/terrain-to-mesh-195349)

### Photon Network

大学时曾经用过的多人开发框架，针对Unity足够简洁高效，学习门槛低。

**Photon Network** 是一个跨平台的实时多人游戏开发框架，广泛应用于 Unity 游戏开发中。它提供了高效且易于使用的工具，使开发者能够轻松实现多人在线互动、同步以及网络通信。不过可自定义和拓展性没那么高，但是一版情况以及足够使用了。

**Photon Network** 的主要特点包括：

1. **实时多人游戏支持**：Photon 提供了一个可靠的架构来处理实时多人游戏的需求，包括玩家匹配、游戏状态同步、消息传递等。
2. **跨平台兼容性**：Photon 支持多个平台，包括 PC、移动设备、WebGL 和主机，开发者可以实现跨平台多人游戏，保证不同设备之间的顺畅互联。
3. **高效的同步机制**：Photon 提供了同步功能，可以确保所有玩家在同一游戏状态下进行游戏。无论是玩家的位置、动画状态，还是其他游戏元素，都可以在网络上同步更新。
4. **房间和匹配系统**：Photon 提供了一个内建的房间和匹配系统，允许玩家加入不同的游戏房间，进行匹配或者创建私人房间。
5. **可靠的消息传递**：Photon 支持可靠的消息传递系统，可以确保数据的准确性和及时性，适用于游戏中的各种网络事件处理。
6. **低延迟**：Photon 使用了全球数据中心，以减少延迟，提供更流畅的在线游戏体验。
7. **扩展性与自定义**：开发者可以自定义 Photon 的一些功能，如自定义消息类型、扩展房间管理等，灵活性非常高。

总之，**Photon Network** 是一个功能强大且易于集成的多人游戏解决方案，适用于需要多人在线互动的游戏，帮助开发者实现稳定、快速且跨平台的网络游戏体验。

官网：[Gaming Circle](https://www.photonengine.com/gaming#)

资产：[PUN 2 - FREE | 网络 | Unity Asset Store](https://assetstore.unity.com/packages/tools/network/pun-2-free-119922)

### Mirrot NetWork

**Mirror Network** 是一个用于 Unity 的开源网络库，旨在简化多人游戏的开发。它是对 Unity UNet 的一种替代或者演化提升的方案，提供了更灵活和高效的网络解决方案，适合需要实时多人互动的游戏，自定义性极高，非常适合灵活，很适用于可以本地创建局域网联机的游戏。

**Mirror Network** 的主要特点包括：

1. **易于使用**：Mirror 提供了简单易懂的 API，使得开发者可以快速上手，轻松实现网络功能。
2. **高性能**：Mirror 经过优化，能够处理大量玩家的连接和数据传输，适合大规模的多人游戏。
3. **开源**：作为一个开源项目，开发者可以自由地查看、修改和扩展源代码，以满足特定需求。
4. **支持多种网络架构**：Mirror 支持客户端-服务器和点对点（P2P）架构，开发者可以根据游戏需求选择合适的网络模型。
5. **灵活的同步机制**：Mirror 提供了强大的数据同步功能，可以轻松同步游戏对象的状态，确保所有玩家看到一致的游戏场景。
6. **社区支持**：Mirror 拥有活跃的社区，开发者可以在社区中获取帮助、分享经验和获取更新。

总之，**Mirror Network** 是一个功能强大且灵活的网络解决方案，适合 Unity 开发者用于创建实时多人游戏，帮助他们快速实现网络功能并优化游戏体验。

官网：[Mirror Networking – Open Source Networking for Unity](https://mirror-networking.com/)

资产：[Mirror | 网络 | Unity Asset Store](https://assetstore.unity.com/packages/tools/network/mirror-129321)

### MasterServerToolkit

**MasterServerToolkit** 是一个用于 Unity 的网络解决方案，旨在简化多人游戏的服务器管理和匹配系统。它提供了一整套工具，帮助开发者快速搭建和管理游戏服务器，支持玩家的匹配和房间管理。

提供了丰富的网络框架支持：**Fishnet** ,  **uNet** ,  **Mirror Networking** ,  **Forge Remastered** 等

**MasterServerToolkit** 的主要特点包括：

1. **服务器管理**：提供了易于使用的界面和工具，帮助开发者管理游戏服务器，包括启动、停止和监控服务器状态。
2. **数据库支持**：多种数据库的支持和对接都已经实现了。
3. **玩家匹配**：支持玩家的快速匹配功能，允许玩家根据不同的条件（如技能水平、地区等）找到合适的游戏房间。
4. **房间管理**：开发者可以创建和管理游戏房间，支持私人房间和公开房间的设置，方便玩家选择。
5. **跨平台支持**：支持多种平台，确保不同设备上的玩家能够顺利连接和互动。
6. **自定义功能**：开发者可以根据需要扩展和自定义 MasterServerToolkit 的功能，以满足特定的游戏需求。
7. **开源和社区支持**：作为一个开源项目，开发者可以查看和修改源代码，同时也有活跃的社区提供支持和资源。

总之，**MasterServerToolkit** 是一个功能全面的网络解决方案，适合需要快速搭建和管理多人游戏服务器的 Unity 开发者，帮助他们提升游戏的在线体验。

官网：[Home | Master Server Toolkit](https://mst.aevien.ru/)

资产：[Master Server Toolkit | 网络 | Unity Asset Store](https://assetstore.unity.com/packages/tools/network/master-server-toolkit-194832)

### Obi Unified particle physics

**Obi Unified Particle Physics** 是 Unity 中的一个物理引擎插件，主要用于模拟粒子和流体的物理效果（绳索、流体、布料、软体）。它是由 **Obi** 提供的一系列高质量模拟工具中的一部分，旨在实现高精度和高性能的粒子物理效果，广泛应用于实时模拟、游戏、特效以及虚拟现实（VR）和增强现实（AR）等应用场景。

**Obi Unified Particle Physics** 的主要特点包括：

1. **流体和粒子模拟**：Obi 提供了一种基于粒子的流体和软体物体模拟方法，能够模拟各种流体现象，如水、油、气体等，同时也支持类似布料、绳索等物体的物理行为。
2. **统一物理系统**：Obi Unified Particle Physics 提供了一个统一的物理框架，能够让开发者轻松地在同一个系统中同时模拟流体、布料、粒子等物理现象，实现更真实的交互效果。
3. **高精度模拟**：Obi 采用了先进的物理算法和技术，能够提供高精度的物理模拟，适用于需要精细控制和高质量效果的应用。
4. **可扩展性和灵活性**：该插件允许开发者通过自定义材质、力场、碰撞体等方式来调整物理行为，具有很高的灵活性，适应不同的需求和场景。
5. **高效性能**：Obi 在保证高质量模拟的同时，优化了性能，使其能够在多种平台上流畅运行，包括 PC 和移动设备。
6. **易于集成**：Obi 提供了与 Unity 的无缝集成，开发者可以通过简单的配置和 API 调用将其引入到自己的项目中，快速实现粒子物理效果。

总之，**Obi Unified Particle Physics** 是一个强大的粒子物理模拟工具，适用于需要复杂流体和粒子效果的实时应用和游戏，能够帮助开发者实现高度真实的物理表现。

官网：[Obi - Unified Particle Physics for Unity 3D](https://obi.virtualmethodstudio.com/)

资产：[Virtual Method - Asset Store](https://assetstore.unity.com/publishers/5170)

### Unity URP Toon Lit Shader

哎呀谁不喜欢三渲二的卡通画风啊！**Unity URP Toon Lit Shader** 是 Unity 的通用渲染管线（Universal Render Pipeline, URP）中的一种着色器，专门用于实现卡通风格的渲染效果。它结合了卡通渲染的特点和 URP 的高效性能，适合用于制作具有独特视觉风格的游戏。

**主要特点包括**：

1. **卡通风格渲染**：通过使用分段阴影和高对比度的颜色，创建出典型的卡通效果，使得物体看起来更具艺术感。
2. **光照支持**：支持多种光照模式，包括漫反射和高光，使得物体在不同光照条件下仍能保持卡通风格。
3. **可调参数**：提供了多种可调参数，开发者可以根据需要自定义颜色、阴影强度、光泽度等，以实现不同的视觉效果。
4. **性能优化**：作为 URP 的一部分，Toon Lit Shader 经过优化，能够在各种平台上高效运行，适合移动设备和低性能硬件。
5. **易于使用**：可以通过 Unity 的材质编辑器轻松创建和调整材质，适合快速迭代和开发。

官网：

资产：[ColinLeung-NiloCat/UnityURPToonLitShaderExample: A very simple toon lit shader example, for you to learn writing custom lit shader in Unity URP](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample?tab=readme-ov-file)

## To Be Continued...

[marijnz/unity-toolbar-extender: Extend the Unity Toolbar with your own Editor UI code.](https://github.com/marijnz/unity-toolbar-extender)

[I2 Localization | 本地化 | Unity Asset Store](https://assetstore.unity.com/packages/tools/localization/i2-localization-14884?clickref=1100lzTFmczG&utm_source=partnerize&utm_medium=affiliate&utm_campaign=unity_affiliate)

[hecomi/uLipSync: MFCC-based LipSync plug-in for Unity using Job System and Burst Compiler](https://github.com/hecomi/uLipSync)

[Easy Save ✪ Complete Save Game &amp; Data Serializer for Unity](https://moodkie.com/easy-save-unity/)

[Magica Cloth 2 | 物理 | Unity Asset Store](https://assetstore.unity.com/packages/tools/physics/magica-cloth-2-242307)
