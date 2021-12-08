import React from "react";
import { chakra, Box, Flex, useColorModeValue, Heading, Text } from "@chakra-ui/react";
import { convertSecondsToHMS } from "../../utils/convert";

export default function VideoCard({ title, thumbnail, duration }){
  return (
    <Flex
      //bg={useColorModeValue("#F9FAFB", "gray.600")}
      p={3}
      w="full"
      alignItems="center"
      justifyContent="center"
    >
      <Flex
        direction="column"
        justifyContent="center"
        alignItems="center"
        w="sm"
        mx="auto"
      >
        <Box
          bg="gray.300"
          h={40}
          w="full"
          rounded="lg"
          shadow="md"
          bgSize="cover"
          bgPos="center"
          style={{
            backgroundImage:
              `url(http://localhost:8000${thumbnail}`,
          }}
        ></Box>

        <Box
          // w={{ base: 56, md: 64 }}
          w={'85%'}
          bg={useColorModeValue("white", "gray.800")}
          mt={-10}
          shadow="lg"
          rounded="lg"
          overflow="hidden"
        >
          <Heading
            // isTruncated
            noOfLines={2}
            p={1}
            textAlign="center"
            // fontWeight="bold"
            // textTransform="uppercase"
            color={useColorModeValue("gray.800", "white")}
            letterSpacing={1}
            as="h3"
            size='xs'
            overflow={'hidden'}
          >
            {title}
          </Heading>

          <Flex
            alignItems="center"
            justifyContent="space-between"
            py={2}
            px={3}
            bg={useColorModeValue("gray.200", "gray.700")}
          >
            <chakra.span
              // fontWeight="bold"
              color={useColorModeValue("gray.800", "gray.200")}
              fontSize="xs"
            >
              {convertSecondsToHMS(duration)}
            </chakra.span>
            <chakra.button
              bg="gray.800"
              fontSize="xs"
              // fontWeight="bold"
              color="white"
              px={2}
              py={1}
              rounded="lg"
              textTransform="uppercase"
              _hover={{
                bg: useColorModeValue("gray.700", "gray.600"),
              }}
              _focus={{
                bg: useColorModeValue("gray.700", "gray.600"),
                outline: "none",
              }}
            >
              Watch
            </chakra.button>
          </Flex>
        </Box>
      </Flex>
    </Flex>
  );
};
