import React, { Component } from "react";
import "./app.css";

class Menu extends Component {
  constructor(props) {
    super(props);

    this.handleMenu = this.handleMenu.bind(this);
    this.state = {
      menu: "is-inactive"
    };
  }

  handleMenu = () => {
    const menuSwitch =
      this.state.menu === "is-active" ? "is-inactive" : "is-active";
    this.setState({
      menu: menuSwitch
    });
    console.log(menuSwitch);
  };
  render() {
    return (
      <div className="menu section is-paddingless is-pulled-right">
        <a
          id="menu"
          role="button"
          className={"navbar-burger " + this.state.menu}
          aria-label="menu"
          aria-expanded="false"
          onClick={this.handleMenu}
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
        <div
          id="navbar"
          className={"navbar-menu " + this.state.menu}
          id="navMenu"
        >
          <div className="navbar-start text">
            <a href="https://xandev.codes/" className="navbar-item">
              Blog - Alexandre
            </a>
            <a
              href="https://gitlab.com/XandeCoding/Tabela-Periodica"
              className="navbar-item"
            >
              Repositório do projeto
            </a>
          </div>
        </div>
      </div>
    );
  }
}

export default Menu;
