import React, { Component } from 'react';
import ImageUploader from 'react-images-upload';

class ImageUpload extends Component {
  render() {
    return(
      <div className="loader">
      {
        this.props.image ?
        <img src={this.props.image}></img> :
        <ImageUploader
                withIcon={true}
                buttonText='Choose images'
                onChange={this.props.onImageUpload}
                imgExtension={['.jpg', '.gif', '.png', '.gif']}
                maxFileSize={5242880}
            />
      }
      </div>
    )
  }
}

export default ImageUpload;
