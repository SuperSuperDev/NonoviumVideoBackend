import React, { useEffect } from "react";
import Plyr from "plyr-react";
import "plyr-react/dist/plyr.css";

function PlyrReact( videoSources ) {
  // console.log(`videoSources`, videoSources)


    const videoSrc = {
      type: "video",
      sources: videoSources.videoSources.map(vidsrc => {
        return {
          src: `http://localhost:8000${vidsrc.file}`,
          width: `${vidsrc.width}`,
          height: `${vidsrc.height}`,
        }
      })
    }

    const videoOptions = {

      quality: {
        default: 720,
        options: [1920, 1080, 720, 480, 360, 240]
        }
    }

    console.log('videoSrc :>> ', videoSrc);
    console.log('videoOptions :>> ', videoOptions);



  return (
    <>
      <Plyr
        source={videoSrc}
        options={videoOptions}
        type="video"
        />
    </>
  )
}

export default PlyrReact;
