# leitstand-robot-contract

The contract between the leitstand backend and the robots: Protobuf messages
(`leitstand.robot.v1`).

## Layout

```
proto/leitstand/robot/v1/
  mission.proto           # mission + dispatch/cancel
  mission_state.proto     # execution state
  factsheet.proto         # capability declaration
  telemetry.proto         # robot telemetry
```

Generated Python stubs are committed under `gen/`.

## Transport (Zenoh)

The proto defines the messages. This section maps each to a Zenoh key. Keys are
namespaced under `leitstand/robot/<id>/`, where `<id>` identifies the robot, so
no message carries a robot id. Payloads are proto canonical JSON.

| Message | Key | Zenoh op |
|---|---|---|
| MissionDispatchRequest / Response | `mission/_action/send_goal` | get |
| CancelRequest | `mission/_action/cancel_goal` | get |
| pause / resume | `instant/pause`, `instant/resume` | put |
| MissionState | `mission/state` | put |
| Factsheet | `factsheet` | get |
| Pose | `pose` | put |
| Battery | `battery` | put |

## Conformance

A conforming robot must:

- Reject the entire mission when a stage has an unknown kind or empty waypoints.
- Treat dispatch as idempotent on `run_id`: re-dispatching the run being
  executed is acknowledged without re-execution; dispatching a different run
  while one is running is rejected. A `run_id` names one execution, so a second
  run of the same mission is a new job with a new id.
- Order `MissionState` frames by `header_id`.

## Versioning

Additive-only within `v1`; a breaking change means `v2`. Enforced by `buf breaking`.

## Development

Requires [buf](https://buf.build).

```
buf lint
buf format -d
buf build
buf generate    # regenerate gen/ and commit it
```

## License

Copyright 2026 Osnabrück University of Applied Sciences.
Apache License 2.0, see [LICENSE](LICENSE).
