
import React, { useEffect, useRef } from 'react';
import fluidPlayer from 'fluid-player'

class MyVideo extends React.Component {
  constructor(props) {
    super(props);
    this.self = React.createRef();
    this.player = null;
  }

  render() {
    return <video ref={this.self}>
      <source src='https://cdn.fluidplayer.com/videos/valerian-1080p.mkv'
              data-fluid-hd
              title='1080p'
              type='video/mp4'/>
    </video>;
  }

  componentDidMount() {
    this.player = fluidPlayer(this.self.current);
  }

  componentWillUnmount() {
    if (!!this.player) {
      this.player.destroy();
    }
  }
}

function FluidPlayer() {
  return <MyVideo />;
}

export default FluidPlayer;
