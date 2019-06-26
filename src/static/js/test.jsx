import React from "react";

export class Test extends React.Component {
    constructor(props) {
        super(props);
    }


    render() {
        return (
            <div className="panel panel-default">
                <div className="panel-heading">This is a React Component</div>
                <div className="panel-body app-text">
                    It says "Hello!"
                </div>
            </div>
        )
    }
}