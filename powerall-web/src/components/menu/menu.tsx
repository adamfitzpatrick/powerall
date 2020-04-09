import * as React from 'react'
import Fab from '@material-ui/core/Fab'

import { Timeframe } from '@components'
import * as styles from './menu.css'
import { DateSelection } from '@models'
import { Downloader } from '../downloader/downloader'

interface MenuProps {
    dateSelection: DateSelection | null
    setDateSelection: (dateSelection: DateSelection | null) => void
}

export function Menu ({ dateSelection, setDateSelection }: MenuProps) {
    const [open, setOpen] = React.useState<boolean>(false)

    const onClick = () => setOpen(true)

    const onClose = (dateSelection: DateSelection | null) => {
        setDateSelection(dateSelection)
        setOpen(false)
    }

    return (
        <div className={styles.menu}>
            <Fab color='primary' onClick={onClick}>
                <span className='material-icons'>settings</span>
            </Fab>
            <Downloader dateSelection={dateSelection} />
            <Timeframe open={open} onClose={onClose} dateSelection={dateSelection} />
        </div>
    )
}