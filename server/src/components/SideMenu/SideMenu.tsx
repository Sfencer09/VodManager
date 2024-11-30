'use client';

import { useIsMobile } from "@/hooks/useIsMobile";
import { colorCodes } from "@/utils/themes/colors";
import { Link } from "@chakra-ui/next-js";
import { Box } from "@chakra-ui/react";
import { Menu } from "@deemlol/next-icons";
import styled from "@emotion/styled";
import { usePathname } from "next/navigation";
import { useState } from "react";

const sideMenuItems: {name: string; path: string; }[] = [{
    name: 'Renders',
    path: '/renders'
},
{
    name: 'Streamers',
    path: '/streamers'
},
{
    name: 'Downloaded Streams',
    path: '/vods',
}];

const MenuWrapper = styled(Box)`
    background-color: ${colorCodes.menuBackground};
    color: ${colorCodes.menuFontColor};
    width: 100px;
    padding: 10px;
    position: absolute;
    left: 0;
    top: 0;
    height: 100vh;
`

const MenuWrapperMobile = styled(Box)`
    background-color: ${colorCodes.menuBackground};
    color: ${colorCodes.menuFontColor};
    width: 12rem;
    padding: 6px;
    position: absolute;
    left: 0;
    top: 0;
    height: 100vh;
`

const MenuButtonMobile = styled(Box)`
    background-color: ${colorCodes.menuBackground};
    color: ${colorCodes.menuFontColor};
    position: fixed;
    top: 4vw;
    left: 4vw;
    width: 8vw;
    height: 8vw;
    border-radius: 4vw;
`


const SideMenuMobile = ({pathname}: {pathname: string}) => {
    const [isExpanded, setIsExpanded] = useState(false);

    return isExpanded ? <MenuWrapperMobile>
        <Menu position='absolute' top='4vw' right='4vw' onClick={() => setIsExpanded(false)}/>
        {sideMenuItems.map((item, index) => {
        <Link href={item.path} key={`sidemenu-${index}`}>{item.name}</Link>
        })}
    </MenuWrapperMobile> : <MenuButtonMobile onClick={() => setIsExpanded(true)}><Menu color={'white'} size={40} /></MenuButtonMobile>
}

export const SideMenu = () => {
    const pathname = usePathname();
    const mobile = useIsMobile();

    return mobile ? <SideMenuMobile pathname={pathname}/> : <MenuWrapper>
        
    </MenuWrapper>
}
