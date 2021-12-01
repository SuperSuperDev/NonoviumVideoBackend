import { getAllVideos, getVideoPost } from "../api/nonoviumVideo"


function videoPost({ videoPost }) {
  return (
    <ul>
      <li>{videoPost.title}</li>
    </ul>
  )
  }

export async function getStaticPaths() {
  const videoPosts = await getAllVideos()
  console.log(`videoPosts for singular`, videoPosts)
  const paths = videoPosts.props.videoPosts.map(videoPost => ({
    params: { postId: videoPost.postId },
  }))
  console.log(`paths`, paths)

  return {
    paths,
    fallback: false,
  }
}

export async function getStaticProps({ params }) {
  return getVideoPost(params.postId)
}

export default videoPost
