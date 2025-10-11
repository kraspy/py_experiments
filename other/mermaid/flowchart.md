## [flowchart](https://mermaid.js.org/syntax/flowchart.html)

### Forms
```mermaid
---
title: Title
---
flowchart TD
	first_node[Square **MD**]
	second_node(
		Round _Edge_
	)
	third_node([Stadium-shape])
	fourth_node[[subroutine]]
	fifth_node[(Database)]
	sixth_node((Circle))
	seventh_node{Romb}
	eighth_node[/Parallelogram/]
	
	
	first_node --> second_node --> third_node --> fourth_node
	fifth_node --> sixth_node --> seventh_node --> eighth_node
	
	%% Новый стиль
	A@{ shape: delay, label: "Label" } -->
	B@{ icon: "fa:LiActivity:", label: "Label", form: "circle", pos: "t"} -->
	C@{ img: "https://cdn4.iconfinder.com/data/icons/small-n-flat/24/cat-alt-1024.png", label: "Image Label", pos: "b", h: 60, constraint: "on" }
```

### [Node Links](https://mermaid.js.org/syntax/flowchart.html#selecting-type-of-animation)
```mermaid
flowchart LR
    A --> B --- C ---|Text| D
    E -.- F ==> G ~~~ H
    I --> J & K --> L 
    M & N --> O & P
```

### [Arrow Types](https://mermaid.js.org/syntax/flowchart.html#selecting-type-of-animation)
```mermaid
flowchart LR
    A --o B --x C
```

### [Animation](https://mermaid.js.org/syntax/flowchart.html#selecting-type-of-animation)

```mermaid
flowchart LR
    A e1@==> B
    e1@{ animation: slow }
```

### [Subgraphs](https://mermaid.js.org/syntax/flowchart.html#subgraphs)
```mermaid
flowchart TB
    subgraph t [TOP]
    direction TB
        subgraph first
            direction LR
            B --> C
        end
        subgraph second
            direction LR
            F --> E
        end
        first --- second
    end
    A --> t --> Z
```

### [Interaction](https://mermaid.js.org/syntax/flowchart.html#interaction)
```mermaid
flowchart LR
A --> B
click A href "https://ya.ru"
click B function_name "Tooltip example"
```

### [Styling](https://mermaid.js.org/syntax/flowchart.html#styling-and-classes)
```mermaid
---
config:
    flowchart:
        curve: stepAfter
---
flowchart TB
    classDef myClass fill: blue;

    A --> B & C

    id1[A] --> id2[B]
    style id1 fill:green, stroke: yellow, stroke-width:10
    style id2 fill:#f001, color: yellow, stroke-dasharray: 1 5

    node_id[class]:::myClass
```
### [Font Awesome](https://mermaid.js.org/syntax/flowchart.html#basic-support-for-fontawesome)
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet"/>

```mermaid
flowchart TD
    B["fa:fa-twitter for peace"]
    B-->C[fa:fa-ban forbidden]
    B-->D(fa:fa-spinner)
    B-->E(A fa:fa-camera-retro perhaps?)
```