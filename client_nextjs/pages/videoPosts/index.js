import axios from 'axios'
// import next image
import Image from 'next/image'
import Link from 'next/link'
import VideoCard from '../../components/video/VideoCard'
import VideoGrid from '../../components/video/VideoGrid'
import { getAllVideos } from '../api/nonoviumVideo'

function VideoPosts({ videoPosts }){
  return (
    console.log(`videoPosts >>:`, videoPosts),
    // <ul>
    //   {videoPosts?.map((videoPost) => (
    //     <li key={videoPost.id}>
    //       <Link href={`/videoPosts/${encodeURIComponent(videoPost.postId)}`}>
    //       <a><VideoCard key={videoPost.id} title={videoPost.title} thumbnail={videoPost.video.thumbnail} /></a>
    //       </Link>
    //       <br />
    //     </li>

    //   ))}
    // </ul>
    <>
      <VideoGrid videoPosts={videoPosts} />
    </>
  )
}

// const token = '4e95e5d2c9b43120fc7dbf7f46e1f1ef1f1776db'
// function headers() {

//   return {
//     headers: {
//       ContentType: 'application/json',
//       Authorization: `Token ${token}`
//     },
//   }
// }

export default VideoPosts

export async function getStaticProps() {
  return getAllVideos()
}



// export async function getStaticProps() {
//   const res = await axios.get('http://localhost:8000/api/videos/', headers())
//   console.log(`res`, res)
//   const videoPosts = await res.data
//   console.log(`videoPost.video`, videoPosts)
//   return {
//     props: {
//       videoPosts
//     }
//   }
// }
