import * as React from 'react'
import 'date-fns'
import DateFnsUtils from '@date-io/date-fns'
import Button from '@material-ui/core/Button'
import Drawer from '@material-ui/core/Drawer'
import Fab from '@material-ui/core/Fab'
import {
    MuiPickersUtilsProvider,
    KeyboardDatePicker
} from '@material-ui/pickers'

import * as styles from './timeframe.css'
import { DateSelection } from '@models'

interface TimeframeProps {
    open: boolean
    onClose: (dateSelection: DateSelection | null) => void
    dateSelection: DateSelection | null
}

export function Timeframe ({ open, onClose, dateSelection }: TimeframeProps) {
    const [ startDate, setStartDate ] = React.useState<Date | null>(dateSelection && dateSelection.startDate)
    const [ endDate, setEndDate ] = React.useState<Date | null>(dateSelection && dateSelection.endDate)

    React.useEffect(() => {
        if (startDate && (!endDate || endDate < startDate)) {
            handleEndSelection(startDate)
        }
    }, [startDate])

    React.useEffect(() => {
        if (endDate && (!startDate || endDate < startDate)) {
            handleStartSelection(endDate)
        }
    }, [endDate])

    const stripTime = (date: Date, end?: boolean) => {
        const stripped = new Date(date)
        stripped.setHours(end ? 23: 0)
        stripped.setMinutes(end ? 59: 0)
        stripped.setSeconds(end ? 59.999 : 0)
        return stripped
    }

    const handleStartSelection = (date: Date) => {
        setStartDate(stripTime(date))
    }

    const handleEndSelection = (date: Date) => {
        setEndDate(stripTime(date, true))
    }

    const handleClearDates = () => {
        setStartDate(null)
        setEndDate(null)
        onClose(null)
    }

    const handleClose = () => {
        if (startDate && endDate) {
            onClose({ startDate, endDate })
            return
        }
        onClose(null)
    }

    return (
        <div className={styles.timeframe}>
            <Drawer anchor='left' open={open}>
                <div className={styles.content}>
                    <MuiPickersUtilsProvider utils={DateFnsUtils}>
                        <div className={styles.datePickerRow}>
                            <KeyboardDatePicker
                                disableToolbar
                                variant='inline'
                                margin="normal"
                                id="start-date-picker"
                                label="Start"
                                format="MM/dd/yyyy"
                                value={startDate}
                                onChange={handleStartSelection}
                                autoOk={true}
                                KeyboardButtonProps={{
                                    'aria-label': 'change date',
                                }}
                            />
                        </div>
                        <div className={styles.datePickerRow}>
                            <KeyboardDatePicker
                                disableToolbar
                                variant='inline'
                                margin="normal"
                                id="end-date-picker"
                                label="End"
                                format="MM/dd/yyyy"
                                value={endDate}
                                onChange={handleEndSelection}
                                autoOk={true}
                                KeyboardButtonProps={{
                                    'aria-label': 'change date',
                                }}
                            />
                        </div>
                    </MuiPickersUtilsProvider>
                    <Button
                        color="secondary"
                        onClick={handleClearDates}
                    >
                        clear dates
                    </Button>
                    <Fab color='primary' onClick={handleClose}>
                        <span className='material-icons'>check</span>
                    </Fab>
                </div>
            </Drawer>
        </div>
    )
}