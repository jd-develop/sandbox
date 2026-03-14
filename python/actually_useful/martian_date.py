#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# martian_date: converts an Earth UTC date to a Martian MTC one.
# Works only for dates after E2017-01-01T00:00Z (E for Earth)
# The earth dates in this file follow the ISO 8601 format, but with
# the prefix 'E'.

# HOW TO UPDATE THIS PROGRAM IF A LEAP SECOND IS ADDED?
# --> Simply add 1 to the LEAP_SECONDS constant
# Note: at the time of writting, last leap second was E2016-12-31T23:59:60Z
# Note: last updated: 2026-01-06 (Bulletin C no. 71)

import time

JULIAN_DATE_UT_UNIX_EPOCH  = 2_440_587.5  # julian date (UT) at UNIX Epoch
JULIAN_DATE_TT_J2000_EPOCH = 2_451_545  # julian date (TT) at J2000 Epoch
MILLISECONDS_A_DAY         = 8.64e7  # how many milliseconds in a day
LEAP_SECONDS               = 37+32.184  # leap seconds since E2017-01-01T00:00Z
ΔJ2000_0                   = 4.5  # E2000-01-06T00:00Z
JULIAN_DAY_MSD_RATIO       = 1.027491252
MSD_EPOCH                  = 44796  # Compared to E2000-01-06T00:00Z
                                    # Corresponds to E1873-12-29
MIDNIGHT_SYNC_ERROR        = 0.0009626  # error (exprimed in MSD) between
                                        # E2000-01-06T00:00Z and the actual
                                        # MTC midnight
MARS_YEAR_LEN              = 668.5991  # in sols
MARS_YEAR_12_EPOCH         = 36247.14279857335  # in sols


def _unix_seconds_to_j2000(time: float):
    """
    Converts Earth time (`time` in seconds since UNIX Epoch) into
    ΔJ2000 (number of julian days (Terrestrial Time) elapsed since
    E2000-01-01T00:00Z)
    """
    time_millis = time*1000  # milliseconds since UNIX Epoch (unit: millisecond)
    # julian date according to UTC (i.e. WITHOUT leap seconds)
    # unit: day
    julian_date_UT = JULIAN_DATE_UT_UNIX_EPOCH + time_millis/MILLISECONDS_A_DAY
    # julian date in Terrestrial Time (i.e. WITH leap seconds)
    # unit: day
    julian_date_TT = julian_date_UT + LEAP_SECONDS/86400
    # days since J2000 Epoch
    # unit: day
    time_J2000 = julian_date_TT - JULIAN_DATE_TT_J2000_EPOCH
    return time_J2000


def earth_to_mars(time: float):
    """
    Converts Earth time (`time`) into MSD (Mars Sol Date)
    `time` is in UNIX time (seconds since UNIX Epoch)
    """
    time_J2000 = _unix_seconds_to_j2000(time)
    # Mars sol date (MSD)
    # At E2000-01-06T00:00Z (ΔJ2000 = 4.5), it was approximately midnight at the
    # Mars prime meridian (MT00:00Z)
    # The ratio between a julian day and a sol is 1.027491252.
    # By convention, the MSD Epoch is 44796 sols before E2000-01-06T00:00Z
    msd = (time_J2000-ΔJ2000_0)/JULIAN_DAY_MSD_RATIO + MSD_EPOCH \
            - MIDNIGHT_SYNC_ERROR
    return msd


def msd_to_mtc(msd: float):
    """
    Converts MSD (Mars Sol Date) to MTC (Mars Coordinated Time) under the form
    (hour, minute, second, millisecond) – please bear in mind that those are
    not SI hours, minutes, seconds and milliseconds!
    """
    hours_float = (24*msd)%24
    hours = int(hours_float)
    minutes_float = (hours_float*60)%60
    minutes = int(minutes_float)
    seconds_float = (minutes_float*60)%60
    seconds = int(seconds_float)
    millis = (seconds_float*1000)%1000
    return (hours, minutes, seconds, millis)


def year(msd: float):
    """
    Converts MSD (Mars Sol Date) to Mars Year (with Year 12 starting at
    E1975-12-19T04:00Z)
    """
    return (msd - MARS_YEAR_12_EPOCH)/MARS_YEAR_LEN + 12


def year_sol_number(msd: float):
    """
    Converts MSD (Mars Sol Date) to the sol number in year (where the first
    sol of the year is sol 1)
    """
    return int((msd - MARS_YEAR_12_EPOCH)%MARS_YEAR_LEN + 1)


def datetime(msd: float):
    """
    Converts MSD (Mars Sol Date) to a Mars datetime
    (year, sol, hour, minute, second)
    """
    hour, minute, second, _ = msd_to_mtc(msd)
    return (int(year(msd)), year_sol_number(msd), hour, minute, second)


def as_french_string(msd: float):
    """
    Converts MSD (Mars Sol Date) to a French string under the form
    "Sol SSS an YY, HH:MM:SS"
    """
    hour, minute, second, _ = msd_to_mtc(msd)
    shour = str(hour).rjust(2, '0')
    sminute = str(minute).rjust(2, '0')
    ssecond = str(second).rjust(2, '0')
    return f"Sol {year_sol_number(msd)} an {int(year(msd))}, {shour}:{sminute}:{ssecond}"

print(as_french_string(earth_to_mars(time.time())))
