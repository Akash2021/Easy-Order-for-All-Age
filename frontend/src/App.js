import React, { Component } from 'react';
import './App.css';
import TitleBar from './components/MainView/TitleBar'
import ContentArea from './components/MainView/ContentArea'

class App extends Component {
  state =  {
    defaultSizeValues: {
      headerFont: {
        value: 2,
        type: 'em'
      },
      contentFont: {
        value: 2,
        type: 'em'
      },
    },
    sizeValues: {
      headerFont: {
        value: 2,
        type: 'em'
      },
      contentFont: {
        value: 2,
        type: 'em'
      },
    }
  }

  resizeValues = (scale) => {
    let sizeValues = this.state.sizeValues;
    for(let key in sizeValues) {
      sizeValues[key].value = this.state.defaultSizeValues[key].value*scale;
    }
    return sizeValues;
  }

  calcScale = (age) => {
    let scale = 1;
    switch (true) {
      case (age>30):
        scale = 1.1
        break;
    }

    return scale;
  }

  onImageUpload = (pictureElem, base64) => {
    let scale = 1;
    let values = this.resizeValues(1.3);
    this.setState({
      image: base64[0],
      sizeValues: values
    })
  }

  render() {
    return (
      <div className="App">
        <TitleBar sizeValues={this.state.sizeValues}/>
        <ContentArea onImageUpload={this.onImageUpload}
                     sizeValues={this.state.sizeValues}
                     image={this.state.image}
                     />
      </div>
    );
  }
}

export default App;
