import React, { Component } from "react";
import SearchBar from "./SearchBar";
import Menu from "./Menu";

import "./app.css";

class App extends Component {
  state = {
    search: ""
  };

  setSearchKey = search => {
    this.setState(state => {
      return { search: search };
    });
  };

  render() {
    const { search } = this.state;

    return (
      <body className="background">
        <Menu />
        <div className="section ">
          <SearchBar setSearchKey={this.setSearchKey} />
        </div>
      </body>
    );
  }
}

export default App;
