@ stub I_BrowserDebugCall
@ stub I_BrowserDebugTrace
@ stdcall I_BrowserQueryEmulatedDomains(wstr ptr ptr) I_BrowserQueryEmulatedDomains
@ stub I_BrowserQueryOtherDomains
@ stub I_BrowserQueryStatistics
@ stub I_BrowserResetNetlogonState
@ stub I_BrowserResetStatistics
@ stub I_BrowserServerEnum
@ stdcall I_BrowserSetNetlogonState(wstr wstr wstr long) I_BrowserSetNetlogonState
@ stub I_NetAccountDeltas
@ stub I_NetAccountSync
@ stub I_NetDatabaseDeltas
@ stub I_NetDatabaseRedo
@ stub I_NetDatabaseSync
@ stub I_NetDatabaseSync2
@ stub I_NetDfsCreateExitPoint
@ stub I_NetDfsCreateLocalPartition
@ stub I_NetDfsDeleteExitPoint
@ stub I_NetDfsDeleteLocalPartition
@ stub I_NetDfsFixLocalVolume
@ stub I_NetDfsGetVersion
@ stub I_NetDfsIsThisADomainName
@ stub I_NetDfsModifyPrefix
@ stub I_NetDfsSetLocalVolumeState
@ stub I_NetDfsSetServerInfo
@ stub I_NetGetDCList
@ stub I_NetListCanonicalize
@ stub I_NetListTraverse
@ stub I_NetLogonControl
@ stub I_NetLogonControl2
@ stub I_NetLogonSamLogoff
@ stub I_NetLogonSamLogon
@ stub I_NetLogonUasLogoff
@ stub I_NetLogonUasLogon
@ stub I_NetNameCanonicalize
@ stub I_NetNameCompare
@ stub I_NetNameValidate
@ stub I_NetPathCanonicalize
@ stub I_NetPathCompare
@ stub I_NetPathType
@ stub I_NetServerAuthenticate
@ stub I_NetServerAuthenticate2
@ stub I_NetServerPasswordSet
@ stub I_NetServerReqChallenge
@ stub I_NetServerSetServiceBits
@ stub I_NetServerSetServiceBitsEx
@ stub NetAlertRaise
@ stub NetAlertRaiseEx
@ stdcall NetApiBufferAllocate(long ptr) NetApiBufferAllocate
@ stdcall NetApiBufferFree(ptr) NetApiBufferFree
@ stdcall NetApiBufferReallocate(ptr long ptr) NetApiBufferReallocate
@ stdcall NetApiBufferSize(ptr ptr) NetApiBufferSize
@ stub NetAuditClear
@ stub NetAuditRead
@ stub NetAuditWrite
@ stub NetBrowserStatisticsGet
@ stub NetConfigGet
@ stub NetConfigGetAll
@ stub NetConfigSet
@ stub NetConnectionEnum
@ stub NetDfsAdd
@ stub NetDfsEnum
@ stub NetDfsGetInfo
@ stub NetDfsManagerGetConfigInfo
@ stub NetDfsMove
@ stub NetDfsRemove
@ stub NetDfsRename
@ stub NetDfsSetInfo
@ stub NetEnumerateTrustedDomains
@ stub NetErrorLogClear
@ stub NetErrorLogRead
@ stub NetErrorLogWrite
@ stub NetFileClose
@ stub NetFileEnum
@ stub NetFileGetInfo
@ stub NetGetAnyDCName
@ stdcall NetGetDCName(wstr wstr ptr) NetGetDCName
@ stub NetGetDisplayInformationIndex
@ stub NetGroupAdd
@ stub NetGroupAddUser
@ stub NetGroupDel
@ stub NetGroupDelUser
@ stub NetGroupEnum
@ stub NetGroupGetInfo
@ stub NetGroupGetUsers
@ stub NetGroupSetInfo
@ stub NetGroupSetUsers
@ stub NetLocalGroupAdd
@ stub NetLocalGroupAddMember
@ stub NetLocalGroupAddMembers
@ stub NetLocalGroupDel
@ stub NetLocalGroupDelMember
@ stub NetLocalGroupDelMembers
@ stub NetLocalGroupEnum
@ stub NetLocalGroupGetInfo
@ stub NetLocalGroupGetMembers
@ stub NetLocalGroupSetInfo
@ stub NetLocalGroupSetMembers
@ stub NetMessageBufferSend
@ stub NetMessageNameAdd
@ stub NetMessageNameDel
@ stub NetMessageNameEnum
@ stub NetMessageNameGetInfo
@ stdcall NetQueryDisplayInformation(wstr long long long long ptr ptr) NetQueryDisplayInformation
@ stub NetRemoteComputerSupports
@ stub NetRemoteTOD
@ stub NetReplExportDirAdd
@ stub NetReplExportDirDel
@ stub NetReplExportDirEnum
@ stub NetReplExportDirGetInfo
@ stub NetReplExportDirLock
@ stub NetReplExportDirSetInfo
@ stub NetReplExportDirUnlock
@ stub NetReplGetInfo
@ stub NetReplImportDirAdd
@ stub NetReplImportDirDel
@ stub NetReplImportDirEnum
@ stub NetReplImportDirGetInfo
@ stub NetReplImportDirLock
@ stub NetReplImportDirUnlock
@ stub NetReplSetInfo
@ stub NetRplAdapterAdd
@ stub NetRplAdapterDel
@ stub NetRplAdapterEnum
@ stub NetRplBootAdd
@ stub NetRplBootDel
@ stub NetRplBootEnum
@ stub NetRplClose
@ stub NetRplConfigAdd
@ stub NetRplConfigDel
@ stub NetRplConfigEnum
@ stub NetRplGetInfo
@ stub NetRplOpen
@ stub NetRplProfileAdd
@ stub NetRplProfileClone
@ stub NetRplProfileDel
@ stub NetRplProfileEnum
@ stub NetRplProfileGetInfo
@ stub NetRplProfileSetInfo
@ stub NetRplSetInfo
@ stub NetRplSetSecurity
@ stub NetRplVendorAdd
@ stub NetRplVendorDel
@ stub NetRplVendorEnum
@ stub NetRplWkstaAdd
@ stub NetRplWkstaClone
@ stub NetRplWkstaDel
@ stub NetRplWkstaEnum
@ stub NetRplWkstaGetInfo
@ stub NetRplWkstaSetInfo
@ stub NetScheduleJobAdd
@ stub NetScheduleJobDel
@ stub NetScheduleJobEnum
@ stub NetScheduleJobGetInfo
@ stub NetServerComputerNameAdd
@ stub NetServerComputerNameDel
@ stub NetServerDiskEnum
@ stub NetServerEnum
@ stub NetServerEnumEx
@ stub NetServerGetInfo
@ stub NetServerSetInfo
@ stub NetServerTransportAdd
@ stub NetServerTransportAddEx
@ stub NetServerTransportDel
@ stub NetServerTransportEnum
@ stub NetServiceControl
@ stub NetServiceEnum
@ stub NetServiceGetInfo
@ stub NetServiceInstall
@ stub NetSessionDel
@ stub NetSessionEnum
@ stub NetSessionGetInfo
@ stub NetShareAdd
@ stub NetShareCheck
@ stub NetShareDel
@ stub NetShareDelSticky
@ stub NetShareEnum
@ stub NetShareEnumSticky
@ stub NetShareGetInfo
@ stub NetShareSetInfo
@ stub NetStatisticsGet
@ stub NetUseAdd
@ stub NetUseDel
@ stub NetUseEnum
@ stub NetUseGetInfo
@ stub NetUserAdd
@ stub NetUserChangePassword
@ stub NetUserDel
@ stub NetUserEnum
@ stub NetUserGetGroups
@ stdcall NetUserGetInfo(wstr wstr long ptr) NetUserGetInfo
@ stub NetUserGetLocalGroups
@ stub NetUserModalsGet
@ stub NetUserModalsSet
@ stub NetUserSetGroups
@ stub NetUserSetInfo
@ stub NetWkstaGetInfo
@ stub NetWkstaSetInfo
@ stub NetWkstaTransportAdd
@ stub NetWkstaTransportDel
@ stdcall NetWkstaTransportEnum (wstr long ptr long ptr ptr ptr) NetWkstaTransportEnum
@ stub NetWkstaUserEnum
@ stdcall NetWkstaUserGetInfo(wstr long ptr) NetWkstaUserGetInfo
@ stub NetWkstaUserSetInfo
@ stdcall NetapipBufferAllocate(long ptr) NetApiBufferAllocate
@ stdcall Netbios(ptr) Netbios
@ stub NetpAccessCheck
@ stub NetpAccessCheckAndAudit
@ stub NetpAllocConfigName
@ stub NetpAllocStrFromStr
@ stub NetpAllocStrFromWStr
@ stub NetpAllocTStrFromString
@ stub NetpAllocWStrFromStr
@ stub NetpAllocWStrFromWStr
@ stub NetpApiStatusToNtStatus
@ stub NetpAssertFailed
@ stub NetpCloseConfigData
@ stub NetpCopyStringToBuffer
@ stub NetpCreateSecurityObject
@ stub NetpDbgDisplayServerInfo
@ stub NetpDbgPrint
@ forward NetpDeleteSecurityObject ntdll.RtlDeleteSecurityObject
@ stdcall NetpGetComputerName(ptr) NetpGetComputerName
@ stub NetpGetConfigBool
@ stub NetpGetConfigDword
@ stub NetpGetConfigTStrArray
@ stub NetpGetConfigValue
@ stub NetpGetDomainName
@ stub NetpGetFileSecurity
@ stub NetpGetPrivilege
@ stub NetpHexDump
@ forward NetpInitOemString ntdll.RtlInitAnsiString
@ stub NetpIsRemote
@ stub NetpIsUncComputerNameValid
@ stub NetpLocalTimeZoneOffset
@ stub NetpLogonPutUnicodeString
@ stub NetpNetBiosAddName
@ stub NetpNetBiosCall
@ stub NetpNetBiosDelName
@ stub NetpNetBiosGetAdapterNumbers
@ stub NetpNetBiosHangup
@ stub NetpNetBiosReceive
@ stub NetpNetBiosReset
@ stub NetpNetBiosSend
@ stub NetpNetBiosStatusToApiStatus
@ stub NetpNtStatusToApiStatus
@ stub NetpOpenConfigData
@ stub NetpPackString
@ stub NetpReleasePrivilege
@ stub NetpSetConfigBool
@ stub NetpSetConfigDword
@ stub NetpSetConfigTStrArray
@ stub NetpSetFileSecurity
@ stub NetpSmbCheck
@ stub NetpStringToNetBiosName
@ stub NetpTStrArrayEntryCount
@ stub NetpwNameCanonicalize
@ stub NetpwNameCompare
@ stub NetpwNameValidate
@ stub NetpwPathCanonicalize
@ stub NetpwPathCompare
@ stub NetpwPathType
@ stub NlBindingAddServerToCache
@ stub NlBindingRemoveServerFromCache
@ stub NlBindingSetAuthInfo
@ stub RxNetAccessAdd
@ stub RxNetAccessDel
@ stub RxNetAccessEnum
@ stub RxNetAccessGetInfo
@ stub RxNetAccessGetUserPerms
@ stub RxNetAccessSetInfo
@ stub RxNetServerEnum
@ stub RxNetUserPasswordSet
@ stub RxRemoteApi
