import axios from "axios";
import dotenv from 'dotenv'
dotenv.config()

const token = process.env.NONOVIUM_TOKEN

const url = process.env.NONOVIUM_API_URL



function headers() {
  return {
    headers: {
      ContentType: 'application/json',
      Authorization: `Token ${token}`
    },
  }
}

export async function getAllVideos() {

const res = await axios.get('http://localhost:8000/api/videoposts/', headers())
const videoPosts = await res.data
  return {
    props: {
      videoPosts
  },
  revalidate: 10

}
}

export async function getVideoPost(postId) {
  const res = await axios.get(`http://localhost:8000/api/videoposts/${postId}/`, headers())
  const videoPost = await res.data
  return {
    props: {
      videoPost
  },
  // revalidate: 10
}
}
