import React from "react";
import ReactDOM from "react-dom";
import {
    BrowserRouter as Router,
    Route,
} from 'react-router-dom'
import {ModuleTree} from "./moduleTree";
import {Test} from "./test";

class App extends React.Component {
    render() {
        return (
            <Router>
                <div>
                    <Route path="(/bcsweb/app.fcgi/modules|/modules)" component={ModuleTree}/>
                    {/*<Route path="(/bcsweb/app.fcgi/|/)" component={Test}/>*/}
                </div>
            </Router>
        )

    }
}


ReactDOM.render(
        <App/>,
        document.getElementById("app"));

