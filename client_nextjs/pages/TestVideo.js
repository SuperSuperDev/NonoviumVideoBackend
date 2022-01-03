import FluidPlayer from "../components/FluidPlayer"





// ReactDOM.render(
//   <ReactHlsPlayer
//     src="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8"
//     autoPlay={false}
//     controls={true}
//     width="100%"
//     height="auto"
//   />,
//   document.getElementById('app')
// );

function TestVideo() {

return (
<FluidPlayer />
)

}



  // return (

  //     <video
  //       controls
  //       autoPlay
  //       src='http://localhost:8000/media/test/test-14101995/playlist.m3u8'
  //     />

  // )
// }
// function testVideo() {
//   const videoSrc = {
//     type: "application/x-mpegURL",
//     sources: {
//       src: 'http://localhost:8000/media/test/test-14101995/playlist.m3u8',
//       width: "640",
//     }
//   }
//   const videoOptions = {

//     quality: {
//     default: 720,
//     options: [1920, 1080, 720, 480, 360, 240]
//     }
//   }


//   return (
//     <>
//       <Plyr
//         source={videoSrc}
//         options={videoOptions}
//         type="video"
//         />
//     </>
//   )
// }
// }
// export default testVideo



export default TestVideo
