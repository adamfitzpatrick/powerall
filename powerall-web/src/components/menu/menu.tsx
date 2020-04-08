import * as React from 'react'
import { Button } from '@rmwc/button'
import '@material/button/dist/mdc.button.css'
import { Fab } from '@rmwc/fab'
import '@material/fab/dist/mdc.fab.css'

import { Timeframe } from '@components'
import * as styles from './menu.css'

export function Menu () {
    const [open, setOpen] = React.useState<boolean>(false)

    const onClick = () => setOpen(!open)

    return (
        <div className={styles.menu}>
            <Fab
                className={styles.button}
                icon='settings'
                onClick={onClick}
            />
            <Fab
                className={styles.button}
                icon='save_alt'
            />
            <Timeframe open={open} onClose={onClick} />
        </div>
    )
}