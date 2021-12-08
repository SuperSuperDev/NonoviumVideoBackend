import { Heading, Text } from "@chakra-ui/react";
import PlyrReact from "../PlyrReact";


export default function VideoPostPage({ videoPost }) {
  const videoSources = videoPost.video.formatSet

  return (
    <>
      <PlyrReact videoSources={videoSources} />
      <Heading
        as="h1"
        fontSize="2xl"
        fontWeight="bold"
        color="gray.900"
        mt="2"
      >
        {videoPost.title}
      </Heading>
      <Text
        as="p"
        fontSize="md"
        color="gray.900"
        mt="2"
      >
        {videoPost.shortDescription}
      </Text>
      <Text
        as="p"
        fontSize="lg"
        color="gray.900"
        mt="2"
      >
        {videoPost.description}
      </Text>

    </>
  );
}
