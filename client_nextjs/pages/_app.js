import '../styles/globals.css'
import { ChakraProvider } from '@chakra-ui/react'
import ChakraUIHeader from '../components/layout/ChakraUIHeader'
import Swibc from '../components/layout/AppSidebar'


function MyApp({ Component, pageProps }) {
  return (
    <ChakraProvider>
      <ChakraUIHeader />

        <Component {...pageProps} />

    </ChakraProvider>
  )
}

export default MyApp
