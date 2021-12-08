import { SimpleGrid } from "@chakra-ui/react";
import VideoCard from "./VideoCard";
import Link from "next/dist/client/link";

export default function VideoGrid({ videoPosts }) {
  return (
    <SimpleGrid minChildWidth={240} spacingX={3} spacingY={3}>
      {videoPosts?.map((videoPost) => (
        // <li key={videoPost.id}>
        <>
          <Link href={`/videoPosts/${encodeURIComponent(videoPost.postId)}`}>
            <a>
              <VideoCard
                key={videoPost.postId}
                title={videoPost.title}
                thumbnail={videoPost.video.thumbnail}
                duration={videoPost.video.duration}
              />
            </a>
          </Link>

        </>
        // </li>
      ))}
    </SimpleGrid>
  );
}
