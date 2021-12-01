import axios from "axios";

const token = process.env.NONOVIUM_TOKEN

const url = process.env.NONOVIUM_API_URL



function headers() {
  return {
    headers: {
      ContentType: 'application/json',
      Authorization: `Token 4e95e5d2c9b43120fc7dbf7f46e1f1ef1f1776db`
    },
  }
}

export async function getAllVideos() {

const res = await axios.get('http://localhost:8000/api/videos/', headers())
const videoPosts = await res.data
  return {
    props: {
      videoPosts
  }
}
}

export async function getVideoPost(postId) {
  const res = await axios.get(`http://localhost:8000/api/videoposts/${postId}/`, headers())
  const videoPost = await res.data
  return {
    props: {
      videoPost
  }
}
}
