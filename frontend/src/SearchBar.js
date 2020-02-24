import React, { Component } from "react";
import Response from "./Response";
import "./app.css";

class SearchBar extends Component {
  constructor(props) {
    super(props);

    this.initialState = {
      search: "",
      sigla: "",
      nome: "Aguardando uma pesquisa...",
      familia: "",
      atomico: "",
      m_molar: ""
    };
    this.state = this.initialState;
  }

  handleChange = event => {
    // TODO: deixar assincrono
    const searchValue = event.target.value;
    this.setState({
      search: searchValue
    });
    console.log(searchValue);
    if (searchValue.length === 0) {
      this.setState(this.initialState);
      console.log("Nenhuma pesquisa está sendo feita");
      return;
    }
    this.props.setSearchKey(searchValue);
    this.searchElement(searchValue);
  };

  searchElement = searchKey => {
    // const searchKey = this.props.searchKey;
    const typeSearch = searchKey.length > 2 ? "elemento" : "sigla";

    const query =
      `{${typeSearch}(name: "${searchKey}")` +
      " {nome, sigla, familia, atomico, m_molar}}";
    console.log(query);

    fetch("http://127.0.0.1:8000/graphql", {
      method: "POST",
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify({
        query: query
      })
    })
      .then(response => response.json())
      .then(response => {
        const element =
          typeSearch === "sigla" ? response.data.sigla : response.data.elemento;
        try {
          this.setState({
            nome: element.nome,
            sigla: element.sigla,
            familia: element.familia,
            atomico: `N.atomico ${element.atomico}`,
            m_molar: `M.molar ${element.m_molar}`
          });
        } catch (err) {
          return `Elemento desconhecido - ${err}`;
        }
      });
  };

  render() {
    return (
      <div className="search-bar">
        <input
          className="input text"
          id="searchBar"
          value={this.state.search}
          onChange={this.handleChange}
          type="text"
          placeholder="Digite a sigla ou o nome do elemento..."
        />
        <div className="response text section">
          <Response {...this.state} />
        </div>
      </div>
    );
  }
}

export default SearchBar;
