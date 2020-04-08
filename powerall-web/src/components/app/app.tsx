import * as React from 'react'
import { Chart, Menu } from '@components'

import * as styles from './app.css'

export const App = () => {
    return (
        <div className={styles.app}>
            <Chart />
            <Menu />
        </div>
    )
}