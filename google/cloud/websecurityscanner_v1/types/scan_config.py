# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1", manifest={"ScanConfig",},
)


class ScanConfig(proto.Message):
    r"""A ScanConfig resource contains the configurations to launch a
    scan.

    Attributes:
        name (str):
            The resource name of the ScanConfig. The name
            follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}'.
            The ScanConfig IDs are generated by the system.
        display_name (str):
            Required. The user provided display name of
            the ScanConfig.
        max_qps (int):
            The maximum QPS during scanning. A valid value ranges from 5
            to 20 inclusively. If the field is unspecified or its value
            is set 0, server will default to 15. Other values outside of
            [5, 20] range will be rejected with INVALID_ARGUMENT error.
        starting_urls (Sequence[str]):
            Required. The starting URLs from which the
            scanner finds site pages.
        authentication (google.cloud.websecurityscanner_v1.types.ScanConfig.Authentication):
            The authentication configuration. If
            specified, service will use the authentication
            configuration during scanning.
        user_agent (google.cloud.websecurityscanner_v1.types.ScanConfig.UserAgent):
            The user agent used during scanning.
        blacklist_patterns (Sequence[str]):
            The excluded URL patterns as described in
            https://cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner#excluding_urls
        schedule (google.cloud.websecurityscanner_v1.types.ScanConfig.Schedule):
            The schedule of the ScanConfig.
        export_to_security_command_center (google.cloud.websecurityscanner_v1.types.ScanConfig.ExportToSecurityCommandCenter):
            Controls export of scan configurations and
            results to Security Command Center.
        risk_level (google.cloud.websecurityscanner_v1.types.ScanConfig.RiskLevel):
            The risk level selected for the scan
        managed_scan (bool):
            Whether the scan config is managed by Web
            Security Scanner, output only.
        static_ip_scan (bool):
            Whether the scan configuration has enabled
            static IP address scan feature. If enabled, the
            scanner will access applications from static IP
            addresses.
    """

    class UserAgent(proto.Enum):
        r"""Type of user agents used for scanning."""
        USER_AGENT_UNSPECIFIED = 0
        CHROME_LINUX = 1
        CHROME_ANDROID = 2
        SAFARI_IPHONE = 3

    class RiskLevel(proto.Enum):
        r"""Scan risk levels supported by Web Security Scanner. LOW
        impact scanning will minimize requests with the potential to
        modify data. To achieve the maximum scan coverage, NORMAL risk
        level is recommended.
        """
        RISK_LEVEL_UNSPECIFIED = 0
        NORMAL = 1
        LOW = 2

    class ExportToSecurityCommandCenter(proto.Enum):
        r"""Controls export of scan configurations and results to
        Security Command Center.
        """
        EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    class Authentication(proto.Message):
        r"""Scan authentication configuration.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            google_account (google.cloud.websecurityscanner_v1.types.ScanConfig.Authentication.GoogleAccount):
                Authentication using a Google account.

                This field is a member of `oneof`_ ``authentication``.
            custom_account (google.cloud.websecurityscanner_v1.types.ScanConfig.Authentication.CustomAccount):
                Authentication using a custom account.

                This field is a member of `oneof`_ ``authentication``.
            iap_credential (google.cloud.websecurityscanner_v1.types.ScanConfig.Authentication.IapCredential):
                Authentication using Identity-Aware-Proxy
                (IAP).

                This field is a member of `oneof`_ ``authentication``.
        """

        class GoogleAccount(proto.Message):
            r"""Describes authentication configuration that uses a Google
            account.

            Attributes:
                username (str):
                    Required. The user name of the Google
                    account.
                password (str):
                    Required. Input only. The password of the
                    Google account. The credential is stored
                    encrypted and not returned in any response nor
                    included in audit logs.
            """

            username = proto.Field(proto.STRING, number=1,)
            password = proto.Field(proto.STRING, number=2,)

        class CustomAccount(proto.Message):
            r"""Describes authentication configuration that uses a custom
            account.

            Attributes:
                username (str):
                    Required. The user name of the custom
                    account.
                password (str):
                    Required. Input only. The password of the
                    custom account. The credential is stored
                    encrypted and not returned in any response nor
                    included in audit logs.
                login_url (str):
                    Required. The login form URL of the website.
            """

            username = proto.Field(proto.STRING, number=1,)
            password = proto.Field(proto.STRING, number=2,)
            login_url = proto.Field(proto.STRING, number=3,)

        class IapCredential(proto.Message):
            r"""Describes authentication configuration for Identity-Aware-
            roxy (IAP).


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                iap_test_service_account_info (google.cloud.websecurityscanner_v1.types.ScanConfig.Authentication.IapCredential.IapTestServiceAccountInfo):
                    Authentication configuration when Web-
                    ecurity-Scanner service account is added in
                    Identity-Aware-Proxy (IAP) access policies.

                    This field is a member of `oneof`_ ``iap_credentials``.
            """

            class IapTestServiceAccountInfo(proto.Message):
                r"""Describes authentication configuration when Web-Security-
                canner service account is added in Identity-Aware-Proxy (IAP)
                access policies.

                Attributes:
                    target_audience_client_id (str):
                        Required. Describes OAuth2 client id of
                        resources protected by Identity-Aware-Proxy
                        (IAP).
                """

                target_audience_client_id = proto.Field(proto.STRING, number=1,)

            iap_test_service_account_info = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="iap_credentials",
                message="ScanConfig.Authentication.IapCredential.IapTestServiceAccountInfo",
            )

        google_account = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="authentication",
            message="ScanConfig.Authentication.GoogleAccount",
        )
        custom_account = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="authentication",
            message="ScanConfig.Authentication.CustomAccount",
        )
        iap_credential = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="authentication",
            message="ScanConfig.Authentication.IapCredential",
        )

    class Schedule(proto.Message):
        r"""Scan schedule configuration.

        Attributes:
            schedule_time (google.protobuf.timestamp_pb2.Timestamp):
                A timestamp indicates when the next run will
                be scheduled. The value is refreshed by the
                server after each run. If unspecified, it will
                default to current server time, which means the
                scan will be scheduled to start immediately.
            interval_duration_days (int):
                Required. The duration of time between
                executions in days.
        """

        schedule_time = proto.Field(
            proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,
        )
        interval_duration_days = proto.Field(proto.INT32, number=2,)

    name = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    max_qps = proto.Field(proto.INT32, number=3,)
    starting_urls = proto.RepeatedField(proto.STRING, number=4,)
    authentication = proto.Field(proto.MESSAGE, number=5, message=Authentication,)
    user_agent = proto.Field(proto.ENUM, number=6, enum=UserAgent,)
    blacklist_patterns = proto.RepeatedField(proto.STRING, number=7,)
    schedule = proto.Field(proto.MESSAGE, number=8, message=Schedule,)
    export_to_security_command_center = proto.Field(
        proto.ENUM, number=10, enum=ExportToSecurityCommandCenter,
    )
    risk_level = proto.Field(proto.ENUM, number=12, enum=RiskLevel,)
    managed_scan = proto.Field(proto.BOOL, number=13,)
    static_ip_scan = proto.Field(proto.BOOL, number=14,)


__all__ = tuple(sorted(__protobuf__.manifest))
