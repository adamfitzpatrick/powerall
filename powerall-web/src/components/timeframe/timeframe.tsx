import * as React from 'react'
import {
    Drawer,
    DrawerHeader,
    DrawerTitle,
    DrawerContent,
    DrawerAppContent
} from '@rmwc/drawer'
import { Fab } from '@rmwc/fab'
import '@material/drawer/dist/mdc.drawer.css'
import '@material/fab/dist/mdc.fab.css'

import * as styles from './timeframe.css'

const drawerStyle: React.CSSProperties = {
    minHeight: '100vh'
}

interface TimeframeProps {
    open: boolean,
    onClose: () => void
}

export function Timeframe ({ open, onClose }: TimeframeProps) {
    return (
        <div className={styles.timeframe}>
            <Drawer modal dismissible open={open}>
                <DrawerHeader>
                    <DrawerTitle>
                        Select data timeframe
                    </DrawerTitle>
                </DrawerHeader>
                <DrawerContent>
                    <div className={styles.content}>
                        <Fab icon='check' onClick={onClose} />
                    </div>
                </DrawerContent>
            </Drawer>
            <DrawerAppContent style={drawerStyle} />
        </div>
    )
}