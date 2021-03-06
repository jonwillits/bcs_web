import React from "react";
import Tree from 'react-d3-tree';

const largeNode = {
    shape: 'rect',
    shapeProps: {
        width: 240,
        height: 50,
        x: -120,
        y: -25,
    },
};

const smallNode = {
    shape: 'rect',
    shapeProps: {
        width: 100,
        height: 50,
        x: -70,
        y: -25,
    }
};

const myTreeData = [
    {
        name: 'BCS-Web',  // this name is used in JS code
        attributes: {
        },
        children: [
            {
                name: 'Intro to BCS',
            },
            {
                name: 'Background and Methods',
                children: [
                    {
                        name: 'Statistical Inference',
                        children: [
                            {
                                name: 'Intro'
                            },
                        ],
                    },
                    {
                        name: 'Research Methods',
                        children: [
                            {
                                name: 'Intro'
                            },
                        ],

                    },
                    {
                        name: 'Programming',
                        children: [
                            {
                                name: 'Intro to Python'
                            },
                            {
                                name: 'Intro to R'
                            },
                            {
                                name: 'Data Visualization'
                            },
                        ],
                    },
                    {
                        name: 'Computational Modeling',
                        children: [
                            {
                                name: 'Intro'
                            },
                        ],

                    },
                ],
            },
            {
                name: 'Subdomains',
                children: [
                    {
                        name: 'Philosophy',
                    },
                    {
                        name: 'Neuroscience',
                    },
                    {
                        name: 'Psychology',
                        children: [
                            {
                                name: 'Introduction',
                            },
                            {
                                name: 'Cognitive',
                                children: [
                                    {
                                        name: 'Introduction',
                                    }]

                            }],
                    },
                    {
                        name: 'Computation and AI',
                    },
                    {
                        name: 'Linguistics',
                    },
                    {
                        name: 'Anthropology',
                    },
                    {
                        name: 'Education',
                    },
                ],
            },
            {
                name: 'Topics',
                children: [
                    {
                        name: 'Concepts and Semantics',
                    },
                    {
                        name: 'Language',
                    },
                ],
            },
        ],
    },
];

const linksStyle = {
    stroke: '#333344',
    strokeWidth: 3,
};

const nodeNameStyle = {
    fontSize: 16,
    strokeWidth: 0,
    textDecoration: 'underline',
};

const leafNodeNameStyle = {
    fontSize: 16,
    strokeWidth: 0,
};

const nodeCircleStyle = {
    fill: 'white',
    strokeWidth: 1,
};

const leafNodeCircleStyle = {
    fill: 'white',
    strokeWidth: 1,
};

const treeStyles = {
    links: linksStyle,
    nodes: {
        node: {
            circle: nodeCircleStyle,
            name: nodeNameStyle,
        },
        leafNode: {
            circle: leafNodeCircleStyle,
            name: leafNodeNameStyle,
        },
    },
};

export class ModuleTree extends React.Component {

    constructor(props) {
        super(props);
        this.state = {xPos: 300, zoom: 0.9};
    }

    /**
     * Calculate and Update state of new xPos
     */
    updatexPos() {
        // 384 is min-width of panel-default
        this.setState({ xPos:  Math.max((384 / 2) - 16, Math.round(window.outerWidth/2 - 116)) });
    }

    // TODO
    updateZoom() {
        let max_width = document.getElementById('treeWrapper').parentElement.offsetWidth;
        this.setState({ zoom:  max_width / 1670 });
        console.log(max_width, max_width / 1670)
    }

    /**
     * Add event listeners
     */
    componentDidMount() {
        this.updatexPos();
        this.updateZoom();
        window.addEventListener("resize", this.updatexPos.bind(this));
        window.addEventListener("resize", this.updateZoom.bind(this));
    }

    /**
     * Remove event listener
     */
    componentWillUnmount() {
        window.removeEventListener("resize", this.updatexPos.bind(this));
        window.removeEventListener("resize", this.updateZoom.bind(this));
    }


    static handleClick(nodeData, e) {
        if (!nodeData._children) {
            console.log(nodeData);
            var parent_names = [nodeData.name.replace(/\s+/g, '_')];
            let n = nodeData;
            console.log(n.parent.name);
            while (n.parent.name !== 'BCS-Web') {
                n = n.parent;
                parent_names.push(n.name.replace(/ /g, '_'))
            }
            const branchName = parent_names.reverse().join('/');
            var url_start = window.location.href.replace('modules', '');
            window.location.href = url_start  + 'module' + '/' + branchName;
        }
    }

    render() {
        return (
            <div id="treeWrapper" style={{width: '100%', height: '700px'}}>
                <Tree data={myTreeData}
                      orientation="vertical"
                      translate={{x:this.state.xPos, y: 40}}  //  dynamic in response to viewport change
                      zoom={this.state.zoom}  // dynamic
                      zoomable={true}
                      scaleExtent = {{min: 0.6, max: 1.0}}
                      pathFunc="straight"
                      initialDepth={1}
                      separation={{siblings: 1.8, nonSiblings: 1.8}}
                      nodeSvgShape={largeNode}
                      textLayout={{textAnchor: "middle", x: 0, y: 0, transform: undefined }}
                      onClick={ModuleTree.handleClick}
                      styles={treeStyles}
                />
            </div>
        )
    }
}