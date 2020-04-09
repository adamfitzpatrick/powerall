import * as React from 'react'
import classnames from 'classnames'
import Fab from '@material-ui/core/Fab'

import { Ina260Measurement, DateSelection } from '@models'
import { load } from '@services'

import * as styles from './downloader.css'

interface DownloaderProps {
    dateSelection: DateSelection | null
}

export function Downloader ({ dateSelection }: DownloaderProps) {
    const [ data, setData ] = React.useState<Ina260Measurement[] | null>(null)

    if (!data) {
        load(dateSelection).then(response => setData(response))
    }
    const blob = new Blob([JSON.stringify(data!)], { type: 'text/plain' })
    const url = window.URL.createObjectURL(blob)
    const filenameDates = dateSelection ? `${dateSelection.startDate.getTime()}-${dateSelection.endDate.getTime()}` : ''
    const filename = `powerall-data-${filenameDates}.json`

    return (
        <Fab style={{ marginTop: '1rem' }} color='primary'>
            <a className={classnames(styles.anchor, 'material-icons')} download={filename} href={url}>save_alt</a>
        </Fab>
    )
}