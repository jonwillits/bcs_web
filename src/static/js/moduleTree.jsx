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
                name: 'Background & Methods',
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
                                name: 'Python'
                            },
                            {
                                name: 'R'
                            },
                            {
                                name: 'Data Visualization'
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
                        name: 'Computation & AI',
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
                        name: 'Concepts & Semantics',
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
        this.state = {xPos: 300};
    }

    /**
     * Calculate & Update state of new xPos
     */
    updatexPos() {
        // alert('window.outerWidth/2' + window.outerWidth/2);
        this.setState({ xPos:  Math.round(window.outerWidth/2 - 100) });
    }

    /**
     * Add event listener
     */
    componentDidMount() {
        this.updatexPos();
        window.addEventListener("resize", this.updatexPos.bind(this));
    }

    /**
     * Remove event listener
     */
    componentWillUnmount() {
        window.removeEventListener("resize", this.updatexPos.bind(this));
    }


    static handleClick(nodeData, e) {
        if (!nodeData._children) {
            console.log(nodeData);
            var parent_names = [nodeData.name.replace(/\s+/g, '_')];
            let n = nodeData;
            console.log(n.parent.name);
            while (n.parent.name !== 'BCS-Web') {
                n = n.parent;
                parent_names.push(n.name.replace(' ', '_'))
            }
            const branchName = parent_names.reverse().join('/');
            var url_start = window.location.href.replace('modules', '');
            window.location.href = url_start  + 'module' + '/' + branchName;
        }
    }

    render() {
        return (
            <div id="treeWrapper" style={{width: this.state.xPos * 2 - 50, height: '700px'}}>
                <Tree data={myTreeData}
                      orientation="vertical"
                      translate={{x:this.state.xPos, y: 40}}  // make dynamic in response to viewport change
                      zoomable={true}
                      scaleExtent = {{min: 1.0, max: 1.0}}
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