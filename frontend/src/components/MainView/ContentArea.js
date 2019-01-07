import React, { Component } from 'react';
import ImageUpload from '../SubViews/ImageUpload'

class ContentArea extends Component {
  render() {
    return(
      <div className="content">
        {this.props.image &&
          <p style={{'fontSize':(this.props.sizeValues.contentFont.value + this.props.sizeValues.contentFont.type)}}>Hi, You seeem to be around {this.props.age} years old. I'm {this.props.percentage}% sure about it!</p>
        }
        <ImageUpload onImageUpload={this.props.onImageUpload} image={this.props.image}/>
      </div>
    )
  }
}

export default ContentArea;
