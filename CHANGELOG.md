# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Added
### Changed
- SDAP-469: Changed tile depth fields to reflect a range of depths for a given tile (min & max).
  - Needed to also add elevation array for masking (Solr can select tiles that overlap spatially if the desired elevation slice goes through all)
- SDAP-486: Renamed tile Z-axis dimension to 'elevation' from 'depth' to standardize how Z-axis is treated in SDAP.
### Deprecated
### Removed
### Fixed
### Security

## [1.0.0] - 2022-12-05
*Initial release of Nexus tile protobuf spec*