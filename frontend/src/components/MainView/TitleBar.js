import React, { Component } from 'react';

class TitleBar extends Component {
  render() {
    return(
      <header>
        <p style={{'fontSize':(this.props.sizeValues.headerFont.value + this.props.sizeValues.headerFont.type)}}>Easy Order for All Age</p>
      </header>
    )
  }
}

export default TitleBar;
