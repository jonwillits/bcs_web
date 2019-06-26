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
        width: 140,
        height: 50,
        x: -70,
        y: -25,
    }
};

// TODO generate tree from directory structure

const myTreeData = [
    {
        name: 'BcsWeb',
        attributes: {
        },
        children: [
            {
                name: 'Introduction',
                children: [
                    {
                        name: 'Intro 1',
                        children: [
                            {
                                name: 'Intro 1a'
                            },
                            {
                                name: 'Intro 1b'
                            },
                            {
                                name: 'Intro 1c'
                            },
                        ],

                    },
                    {
                        name: 'Intro 2'
                    },
                    {
                        name: 'Intro 3'
                    },
                ],
            },
            {
                name: 'Statistics',
            },
            {
                name: 'Modeling',
                children: [
                    {
                        name: 'Neural Networks',
                        children: [
                            {
                                name: 'RNN',
                            },
                            {
                                name: 'CNN',
                            }]
                    },
                    {
                        name: 'Bayesian Models',
                    },
                    {
                        name: 'Deep Learning',
                    },
                ],
            },
            {
                name: 'Semantics',
            },
        ],
    },
];

const linksStyle = {
    stroke: '#333344',
    strokeWidth: 3,
};

const nodeNameStyle = {
    fontSize: 26,
    textDecoration: 'underline',
    strokeWidth: 0,
};

const leafNodeNameStyle = {
    fontSize: 26,
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
            var parent_names = [nodeData.name.replace(' ', '_')];
            let n = nodeData;
            console.log(n.parent.name);
            while (n.parent.name !== 'BcsWeb') {
                n = n.parent;
                parent_names.push(n.name.replace(' ', '_'))
            }
            const branchName = parent_names.reverse().join('+');
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