import { getAllVideos, getVideoPost } from "../api/nonoviumVideo";
import VideoJSPlayer from "../../components/VideoJSPlayer";
import React from 'react'
import ReactPlayer from 'react-player/lazy'
import PlyrReact from "../../components/PlyrReact";
import VideoPostPage from "../../components/video/VideoPostPage";

function videoPost({ videoPost }) {
  // const videoJsOptions = {
  //   autoplay: false,
  //   controls: true,
  //   sources: videoPost.video.formatSet.map((format) => ({
  //     src: `http://localhost:8000${format.file}`,
  //     type: "video/mp4",
  //   })),
  // };
  // console.log(`videoJsOptions`, videoJsOptions);
  // const videoSources = videoPost.video.formatSet.map((format) => (
  //   `http://localhost:8000${format.file}`
  //   ))
  // // // const videoSources = videoPost.video.formatSet

  // console.log(`videoSources`, videoSources)

  return (
    <div>
      <VideoPostPage videoPost={videoPost} />
      {/* <h1>{videoPost.title}</h1>
      <h2>Plyr React</h2>
      <PlyrReact videoSources={ videoSources } /> */}
      {/* <h2>ReactPlayer:</h2>
      <ReactPlayer playing url={ videoSources } controls />
      <h2>PlayerJS</h2>
      <div>
        {videoPost.video.formatSet? <VideoJSPlayer {...videoJsOptions} /> : <div>Loading...</div>}
      </div> */}
    </div>
  );
}

export async function getStaticPaths() {
  const videoPosts = await getAllVideos();
  console.log(`videoPosts for singular`, videoPosts);
  const paths = videoPosts.props.videoPosts.map((videoPost) => ({
    params: { postId: videoPost.postId },
  }));
  console.log(`paths`, paths);

  return {
    paths,
    fallback: false,
  }
}

export async function getStaticProps({ params }) {
  return getVideoPost(params.postId);
}

export default videoPost;
