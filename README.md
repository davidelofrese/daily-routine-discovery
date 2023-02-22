# Process mining with Petri nets: an application to daily routine modeling

This repository contains the event logs and the models discovered for the case study of the Formal Methods in Computer Science course.

The goal of the case study is the practical application of process mining techniques to discover and evaluate a process model, expressed with Petri nets, of the daily routine of a user based on a labeled event log containing the activities carried out during the day. The final report with further details is available [here](report.pdf).

Most of the content of this respository has been generated with [ProM 6](https://promtools.org/). However, the event logs and the models are in standard formats (XES and PNML) which can be imported in other process mining software as well.

## Structure of the repository

The content of this repository is divided in three folders:
- `data` - this folder contains the complete event log in multiple formats (plain text, CSV and XES), in addition to two filtered versions (in XES format)
- `models` - this folder contains three sub-folders, each of them with the models discovered (in PNML format) by various algorithms on three versions of the event log
- `converter` - this folder contains the Python script which has been used to convert the raw event log to a CSV file

## Author

[Davide Lofrese](https://github.com/davidelofrese)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.