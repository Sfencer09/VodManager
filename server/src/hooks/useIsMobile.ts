import { useMediaQuery } from "@chakra-ui/react"

export const mobileWidth = '600px'

export const useIsMobile = () => {
    const [isNotMobile] = useMediaQuery(`(min-width: ${mobileWidth})`, {ssr: true, fallback: false});
    return !isNotMobile;
}

export const useIsMobileChakraUnfriendly = () => {
    const [isMobile] = useMediaQuery(`(max-width: ${mobileWidth})`, {ssr: true, fallback: false});
    return isMobile;
}