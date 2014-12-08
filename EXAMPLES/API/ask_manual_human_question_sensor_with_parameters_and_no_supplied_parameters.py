
"""
Ask a manual question using human strings by referencing the name of a single sensor that takes parameters, but not supplying any parameters (and letting pytan automatically determine the appropriate default value for those parameters which require a value).

No sensor filters, sensor parameters, sensor filter options, question filters, or question options supplied.
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}
kwargs["sensors"] = u'Folder Name Search with RegEx Match'
kwargs["qtype"] = u'manual_human'

# call the handler with the ask method, passing in kwargs for arguments
response = handler.ask(**kwargs)
import pprint, io

print ""
print "Type of response: ", type(response)

print ""
print "Pretty print of response:"
print pprint.pformat(response)

print ""
print "Equivalent Question if it were to be asked in the Tanium Console: "
print response['question_object'].query_text

# create an IO stream to store CSV results to
out = io.BytesIO()

# call the write_csv() method to convert response to CSV and store it in out
response['question_results'].write_csv(out, response['question_results'])

print ""
print "CSV Results of response: "
print out.getvalue()



'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2014-12-08 15:08:08,088 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:13,105 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:18,124 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:23,138 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:28,153 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:33,167 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:38,182 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:43,197 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:48,219 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:53,236 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:08:58,254 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:03,270 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:08,285 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:13,302 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:18,319 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:23,336 INFO     question_progress: Results 0% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:28,359 INFO     question_progress: Results 33% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:33,377 INFO     question_progress: Results 50% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:38,401 INFO     question_progress: Results 67% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:43,421 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:48,437 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:53,455 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:09:58,476 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:10:03,496 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:10:08,515 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:10:13,535 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:10:18,550 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:10:23,569 INFO     question_progress: Results 83% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)
2014-12-08 15:10:28,590 INFO     question_progress: Results 100% (Get Folder Name Search with RegEx Match[No, , No, ] from all machines)

Type of response:  <type 'dict'>

Pretty print of response:
{'question_object': <taniumpy.object_types.question.Question object at 0x10e6367d0>,
 'question_results': <taniumpy.object_types.result_set.ResultSet object at 0x10e539f10>}

Equivalent Question if it were to be asked in the Tanium Console: 
Get Folder Name Search with RegEx Match[No, , No, ] from all machines

CSV Results of response: 
Count,"Folder Name Search with RegEx Match[No, , No, ]"
39525,[too many results]
2,C:\Windows\winsxs\amd64_microsoft-windows-s..structure.resources_31bf3856ad364e35_6.1.7600.16385_en-us_faf46e6f502e00e8
2,C:\Windows\winsxs\x86_microsoft-windows-e..-host-authenticator_31bf3856ad364e35_6.1.7601.17514_none_a7c68343f07f776f
1,C:\Windows\winsxs\amd64_microsoft-windows-ocspsvc_31bf3856ad364e35_6.1.7601.22807_none_3bfeae7293092e4b
1,C:\Windows\winsxs\amd64_microsoft-windows-c..ityclient.resources_31bf3856ad364e35_6.1.7601.22865_en-us_c339d6d6cfb99c39
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\bg\LC_MESSAGES
2,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Xml
1,C:\Users\Jim Olsen\Desktop\SysinternalsSuite
2,C:\Windows\winsxs\amd64_microsoft-windows-scripting.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e72192b67124ad43
2,C:\Windows\winsxs\x86_microsoft-windows-mlang.resources_31bf3856ad364e35_6.1.7600.16385_ru-ru_cf3a10abc52740f6
1,C:\Windows\winsxs\x86_microsoft-windows-directshow-dvdsupport_31bf3856ad364e35_6.1.7601.21987_none_566a88a44b6e5342
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-internetexplorer_31bf3856ad364e35_11.2.9600.17041_none_11e6f4b92ee9bf19
1,C:\Users\Jim Olsen\AppData\Local\Google
2,C:\Windows\winsxs\x86_microsoft-windows-e..nt-client.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e5c3d3ec6ff64de3
2,C:\Windows\winsxs\amd64_microsoft-windows-d..e-eashared-kjshared_31bf3856ad364e35_6.1.7600.16385_none_99b74194b7347cab
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\RadLangSvc
2,C:\Windows\winsxs\amd64_microsoft-windows-p..ginworker.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ae3287fe59b4af28
1,C:\Windows\winsxs\amd64_microsoft-windows-i..riptcollectionagent_31bf3856ad364e35_11.2.9600.17041_none_984c3cbdadb5a971
2,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.ServiceProce#
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_122\grep\share\locale\tr\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_63\grep
1,C:\Windows\Microsoft.NET\assembly\GAC_32\Microsoft.SqlServer.BulkInsertTaskConnections
2,C:\ProgramData\Microsoft\Device Stage\Task\{e35be42d-f742-4d96-a50a-1775fb1a7a42}\en-US
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\Microsoft.S8d1a6405#
2,C:\Windows\assembly\NativeImages_v2.0.50727_64\napsnap
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.B22c61a69#\9a56520d8321e899683663fc7b00b739
2,C:\Windows\winsxs\amd64_microsoft-windows-baseapinamespace_31bf3856ad364e35_6.1.7601.17514_none_a4272f399040a523
1,C:\Windows\System32\inetsrv\config\Export
2,C:\Windows\winsxs\amd64_microsoft-windows-wininit_31bf3856ad364e35_6.1.7600.16385_none_8ce7aa761e01ad49
2,C:\Windows\winsxs\amd64_microsoft-windows-d..x-directxdiagnostic_31bf3856ad364e35_6.1.7601.17514_none_81e99da174638311
1,C:\Windows\winsxs\amd64_netfx-accessibility_b03f5f7f11d50a3a_6.1.7601.22733_none_a079af8fec10f97e
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Dynamic.Runtime
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Workflow.Run#
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_56\grep\share\locale\vi\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00050409_31bf3856ad364e35_6.1.7600.16385_none_765aa38f38767686
2,C:\Windows\winsxs\amd64_microsoft-windows-s..ty-spp-ux.resources_31bf3856ad364e35_6.1.7600.16385_en-us_54dae2e5153375ce
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.Runtime.Remo#\875c35969785fa170d186e7ca546ac9e
1,C:\Windows\winsxs\amd64_microsoft-windows-inetres-adm.resources_31bf3856ad364e35_11.2.9600.17239_en-us_520b80ca92793283
1,C:\Windows\winsxs\amd64_microsoft-windows-b..vironment-os-loader_31bf3856ad364e35_6.1.7601.21655_none_b9ac1d069c83936e
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\WindowsForm0b574481#
2,C:\Windows\winsxs\amd64_microsoft-windows-l..webserver.resources_31bf3856ad364e35_6.1.7601.17514_en-us_c9b90df8dc48cf89
1,C:\Windows\winsxs\wow64_microsoft-windows-scripting-vbscript_31bf3856ad364e35_6.1.7601.18337_none_b0c1f98278f4f2bf
2,C:\Windows\winsxs\amd64_microsoft-windows-f..truetype-lucidasans_31bf3856ad364e35_6.1.7600.16385_none_d0e8774fa1155a53
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_21\grep\share\locale\ja\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-d..s-ime-japanese-core_31bf3856ad364e35_6.1.7600.16385_none_cb604f1aa758e6b6
1,C:\Program Files (x86)\Common Files\microsoft shared\MSEnv\PublicAssemblies
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.S6402eefa#\57e4c4b79ab9ff13194fff26fd4cb81e
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_98\grep\share\locale\hu\LC_MESSAGES
2,C:\Windows\Media\Calligraphy
2,C:\Windows\System32\DriverStore
1,C:\Windows\winsxs\amd64_microsoft-windows-m..do-backcompat-tlb20_31bf3856ad364e35_6.1.7601.22012_none_49c4ab6d21d4e912
2,C:\Windows\winsxs\x86_microsoft-windows-x..ocess-mui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_51e4cd07e2a390ca
2,C:\Windows\winsxs\Temp\PendingRenames
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Windows.D#\5efdf2ce3570caddc09eeae943f71cee
1,C:\Windows\winsxs\amd64_microsoft-windows-m..ents-mdac-ado15-dll_31bf3856ad364e35_6.1.7601.22012_none_6ade6200a065d2ea
1,C:\Windows\assembly\GAC_MSIL\PresentationFramework\3.0.0.0__31bf3856ad364e35
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_24\grep\share\locale\de\LC_MESSAGES
2,C:\Windows\winsxs\amd64_prnlx00x.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_34edc3c5e185ed82
2,C:\Windows\winsxs\x86_microsoft-windows-s..-binaries.resources_31bf3856ad364e35_6.1.7601.17514_sk-sk_3f6dfbca0c1ae0a6
1,C:\Windows\winsxs\x86_system.printing_31bf3856ad364e35_6.1.7601.22309_none_75e11e57ed6f8b6a
2,C:\Windows\winsxs\amd64_microsoft-windows-g..admintools-admfiles_31bf3856ad364e35_6.1.7600.16385_none_0d041ab5a8298266
2,C:\Windows\winsxs\x86_microsoft-windows-n..-security.resources_31bf3856ad364e35_6.1.7600.16385_en-us_4e0c2004a5e71cbd
2,C:\Windows\Microsoft.NET\Framework\v2.0.50727\ASP.NETWebAdminFiles\App_GlobalResources
2,C:\Windows\Microsoft.NET\Framework\v2.0.50727\CONFIG\Browsers
2,C:\Windows\winsxs\x86_microsoft-windows-comctl32-v5.resources_31bf3856ad364e35_6.1.7600.16385_ru-ru_abc131a3483b963e
2,C:\Windows\winsxs\x86_microsoft-windows-i..tional-codepage-858_31bf3856ad364e35_6.1.7600.16385_none_cebddca2fc8602ec
1,C:\Windows\winsxs\amd64_microsoft-windows-t..instationextensions_31bf3856ad364e35_6.1.7601.17828_none_f83075d781b149cb
2,C:\Windows\winsxs\amd64_microsoft-windows-comctl32-v5.resources_31bf3856ad364e35_6.1.7600.16385_th-th_48e4d94ee906cf10
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_19\grep\share\locale\tr\LC_MESSAGES
2,C:\Windows\System32\DriverStore\FileRepository\qd3x64.inf_amd64_neutral_e8903726d63a3f07
2,C:\Windows\winsxs\amd64_sdbus.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_86b03fe7f8988681
1,C:\Windows\winsxs\x86_netfx-netfxsbs10_exe_31bf3856ad364e35_6.1.7601.18514_none_3d9642980c369d84
2,C:\Windows\winsxs\x86_microsoft-windows-r..ne-editor.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b372f75f60a7c3cb
2,C:\Windows\winsxs\amd64_microsoft-windows-pcwdiagnostic_31bf3856ad364e35_6.1.7600.16385_none_5120bf8b19591afa
2,C:\Windows\winsxs\amd64_microsoft-windows-f..overcluster-wizards_31bf3856ad364e35_6.1.7601.17514_none_9e78ebf51945212a
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_23\grep\share\locale\ky\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-eventviewer.resources_31bf3856ad364e35_6.1.7600.16385_en-us_809afd26837a22dc
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_24\grep\share\locale\pt_BR\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-themeservice_31bf3856ad364e35_6.1.7600.16385_none_05f77252e20d9cfd
2,C:\Windows\winsxs\amd64_microsoft-windows-n..ce_datastore_srvsku_31bf3856ad364e35_6.1.7600.16385_none_7ea671bdffc2c389
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_194\grep\bin
2,C:\Windows\assembly\GAC_MSIL\Microsoft.ApplicationId.RuleWizard.Resources
2,C:\Windows\winsxs\amd64_srpuxnativesnapin_31bf3856ad364e35_6.1.7600.16385_none_447807b31b9d298e
1,C:\Windows\assembly\GAC\VSLangProj\7.0.3300.0__b03f5f7f11d50a3a
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.S1eb28fa5#\5661d649208ef3a720c99e1e4271c07a
2,C:\Windows\SysWOW64\en-US\Licenses\OEM\ServerStorageWorkgroup
2,C:\Windows\winsxs\wow64_microsoft-windows-n..etcapture.resources_31bf3856ad364e35_6.1.7600.16385_en-us_243202836fa93a1a
2,C:\Windows\winsxs\x86_microsoft-windows-lsa-msprivs.resources_31bf3856ad364e35_6.1.7600.16385_sv-se_4c5086c9a2727fc3
1,C:\Program Files\Tanium\Tanium Server\ApacheBackup2014-09-16-20-44-23\cgi-bin
2,C:\Windows\winsxs\amd64_microsoft-windows-i..rver2008compat-data_31bf3856ad364e35_6.1.7600.16385_none_07263572e5ebcd9d
2,C:\Windows\System32\DriverStore\FileRepository\adpu320.inf_amd64_neutral_4ea3d42a9839982a
2,C:\Windows\System32\WindowsPowerShell\v1.0\Modules\AppLocker
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_188\grep\share\locale\sl\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.Bfc9dc24d#\5b153cb12d982242817d816f01e63cb4
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_56\grep\share\locale\da\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-t..framework-migration_31bf3856ad364e35_6.1.7600.16385_none_4ce62d7fd1cb54eb
2,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_th-th_8c299c84d28e8005
2,C:\Windows\winsxs\x86_microsoft-windows-mediaplayer-migration_31bf3856ad364e35_6.1.7601.17514_none_e02729035a3379c1
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep
2,C:\Windows\winsxs\x86_microsoft-windows-tapiadmin_31bf3856ad364e35_6.1.7601.17514_none_5fbc6ff536eb243e
1,C:\Windows\winsxs\wow64_microsoft-windows-security-kerberos_31bf3856ad364e35_6.1.7601.18606_none_4f5e488afbc409b9
2,C:\Windows\winsxs\x86_microsoft-windows-sendmail.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ef49195de3a2e11b
2,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-20423_31bf3856ad364e35_6.1.7600.16385_none_ae5b1276ffc4917e
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.Management.RegisteredServers\10.0.0.0__89845dcd8080cc91
2,C:\Windows\winsxs\amd64_microsoft-windows-mediaplayer-wmvsdk_31bf3856ad364e35_6.1.7601.17514_none_04514cd13d40a393
2,C:\Windows\winsxs\amd64_microsoft-windows-m..readwrite.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b212b9dc94b41b2e
1,C:\Windows\winsxs\msil_microsoft.visualbasic_b03f5f7f11d50a3a_6.1.7601.22733_none_6b1e5248d77e003d
2,C:\Windows\winsxs\amd64_server-help-h1s.perfmon.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e6c040e564a18de0
2,C:\Users\Jim Olsen\AppData\Local\Microsoft\Internet Explorer
2,C:\Program Files\VMware\VMware Tools\plugins\vmsvc
1,C:\Windows\winsxs\x86_microsoft-windows-p..age-codec.resources_31bf3856ad364e35_7.1.7601.16492_fr-fr_4522938c0ba39055
1,C:\Windows\winsxs\amd64_microsoft-windows-t..teconnectionmanager_31bf3856ad364e35_6.1.7601.22750_none_ed1f8e488425629d
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_72\grep\man\cat1p
2,C:\Windows\winsxs\amd64_microsoft-windows-fmifs_31bf3856ad364e35_6.1.7600.16385_none_b303632c4b483c6c
2,C:\Windows\winsxs\amd64_microsoft-windows-f..rcluster-powershell_31bf3856ad364e35_6.1.7601.17514_none_f273f11a257acc7b
2,C:\Windows\winsxs\amd64_netfx-mscorpe_dll_b03f5f7f11d50a3a_6.1.7601.17514_none_8492ec5f045f17f3
2,C:\Windows\winsxs\amd64_mdmusrg.inf_31bf3856ad364e35_6.1.7600.16385_none_ef6d0c5fba40766d
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_53\grep\share\locale\es\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-b..tiondata-com-server_31bf3856ad364e35_6.1.7601.17514_none_3dc961517b5bd485
1,C:\Windows\winsxs\amd64_netfx-system.xml_b03f5f7f11d50a3a_6.1.7601.22740_none_4a87840c55cea28e
2,C:\Windows\winsxs\x86_microsoft-windows-com-dtc-setup_31bf3856ad364e35_6.1.7600.16385_none_8da1fd210f4e6422
2,C:\Windows\winsxs\amd64_microsoft-windows-iis-aspbinaries_31bf3856ad364e35_6.1.7601.17514_none_eaaa53b67e14526e
2,C:\Windows\System32\wbem\Logs
1,C:\Windows\winsxs\amd64_microsoft-windows-usp_31bf3856ad364e35_6.1.7601.22666_none_0b75f5788860623d
2,C:\Windows\winsxs\amd64_wcf-icardagt_exe_31bf3856ad364e35_6.1.7600.16385_none_8dcc9c6f8b58a5eb
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Diagnostics.Debug
1,C:\Python27\Lib\encodings
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.A7373a429#\ab9e962308894f7a534dd3aaa055c576
2,C:\Windows\winsxs\amd64_microsoft-windows-server-editions-matrix_31bf3856ad364e35_6.1.7601.17514_none_567c82324e93b3ba
2,C:\Windows\winsxs\amd64_fdwsd_31bf3856ad364e35_6.1.7600.16385_none_d99d751adbd6df3c
2,C:\Windows\SysWOW64\migration\WSMT\rras\dlmanifests\Microsoft-Windows-RasServer-MigPlugin
2,C:\Windows\winsxs\x86_microsoft-windows-p..soundservice-server_31bf3856ad364e35_6.1.7600.16385_none_cdbd3bd8d282195f
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\System.Runteb92aa12#
2,C:\Windows\winsxs\amd64_microsoft-windows-t..n-nonmsil.resources_31bf3856ad364e35_6.1.7601.17514_en-us_1a644c96b184b0fd
2,C:\Windows\assembly\GAC_MSIL\System.Runtime.Serialization.Formatters.Soap\2.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_microsoft-windows-scrnsave_31bf3856ad364e35_6.1.7600.16385_none_3d3492aaf415de8e
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_26\grep\share\locale\fi\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-scripting-jscript9_31bf3856ad364e35_11.2.9600.17239_none_26972afdd2aea099
1,C:\pytan
2,C:\Windows\winsxs\amd64_microsoft-windows-m..ds-ce-rll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6a0dd7ce3b0d1786
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_24\grep\share\locale\ga\LC_MESSAGES
2,C:\Windows\winsxs\wow64_microsoft-windows-i..isapifilterbinaries_31bf3856ad364e35_6.1.7600.16385_none_d2e2c5a7872ef5b5
2,C:\Windows\winsxs\amd64_microsoft-windows-d..anagement.resources_31bf3856ad364e35_6.1.7600.16385_en-us_70bd2df49cbcc5d7
2,C:\Windows\winsxs\wow64_microsoft-windows-p..ll-preloc.resources_31bf3856ad364e35_6.1.7600.16385_en-us_27fbee50ef7f6588
2,C:\Windows\winsxs\x86_microsoft-windows-msmpeg2enc_31bf3856ad364e35_6.1.7601.17514_none_0b450351a4424f06
2,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-00010439_31bf3856ad364e35_6.1.7601.17514_none_f6670d2d9f81941a
1,C:\Windows\winsxs\amd64_microsoft-windows-d2d.resources_31bf3856ad364e35_7.1.7601.16492_de-de_3dc539e9fdc54eb8
1,C:\Users\Jim Olsen\AppData\Local\Google\Chrome\User Data\Default\Extensions\apdfllckaahabafndbhieahigkjlhalf\6.3_0\_metadata
1,C:\Windows\winsxs\amd64_microsoft-windows-k..distribution-center_31bf3856ad364e35_6.1.7601.18658_none_e9b67a55aafd5915
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_63\grep\share\locale\nb\LC_MESSAGES
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_19\grep\contrib\grep\2.5.4\grep-2.5.4-src\doc
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Workflow.ComponentModel\v4.0_4.0.0.0__31bf3856ad364e35
2,C:\Windows\winsxs\amd64_microsoft-windows-f..uster-rhs.resources_31bf3856ad364e35_6.1.7600.16385_en-us_bfb550e4d357a13c
1,C:\Python27\Lib\multiprocessing\dummy
1,C:\Windows\winsxs\amd64_microsoft-windows-windowscodec_31bf3856ad364e35_7.1.7601.16492_none_e5bfce1d42e6e71d
2,C:\Windows\System32\migration
2,C:\Windows\winsxs\x86_microsoft-windows-media-mp3acm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2b0d4dbaf241f90a
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.Smo\10.0.0.0__89845dcd8080cc91
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Printing
2,C:\Windows\winsxs\x86_microsoft-windows-wab-app_31bf3856ad364e35_6.1.7601.17514_none_44b0c76c35d4b76d
2,C:\Windows\winsxs\amd64_microsoft-windows-telephonyserver_31bf3856ad364e35_6.1.7600.16385_none_2a18b42e4b4fec52
2,C:\Windows\System32\migration\en-US
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_193\grep\share\locale\pt_BR\LC_MESSAGES
1,C:\Windows\PCHEALTH\ERRORREP
2,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_ar-sa_25b69e51bf9d09dc
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_122\yara
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\SqlWorkbenchProjectItems\Sql\Earlier Versions\Create Statistics
2,C:\Windows\winsxs\x86_microsoft-windows-s..t-tracker.resources_31bf3856ad364e35_6.1.7600.16385_en-us_25cb0eedc2efe3f8
1,C:\Windows\winsxs\amd64_wcf-icardres_dll_vista_31bf3856ad364e35_6.1.7601.22733_none_6fa639389aa6848a
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_97\grep\manifest
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Linq.Queryable
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Wind0de890be#
2,C:\Windows\winsxs\amd64_adfs-upgrademb-files_31bf3856ad364e35_6.1.7600.16385_none_fbd0c34fcbe686a6
1,C:\Windows\winsxs\amd64_microsoft-windows-cryptnet-dll_31bf3856ad364e35_6.1.7601.22380_none_7579163e2bcf63b6
2,C:\Windows\winsxs\x86_microsoft-windows-m..river-rll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5ad10fe903ded84f
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Linq.Parallel\v4.0_4.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_mdmsun1.inf_31bf3856ad364e35_6.1.7600.16385_none_1f7c98965ef22a0b
2,C:\Windows\assembly\GAC_32\Policy.1.2.Microsoft.Interop.Security.AzRoles
2,C:\Users\Default\Pictures
2,C:\ProgramData\Microsoft\User Account Pictures
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\MSBuild
1,C:\Windows\Microsoft.NET\assembly\GAC_32\WebDev.WebHost40
2,C:\Windows\winsxs\x86_microsoft-windows-v..kprovider.resources_31bf3856ad364e35_6.1.7600.16385_en-us_310eba4283ecd151
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_35\grep\share\locale\sr\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.Data.Entity
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.Management.SystemMetadataProvider
2,C:\Windows\System32\DriverStore\FileRepository\mdmati.inf_amd64_neutral_ded8f26cdee953c3
2,C:\Windows\winsxs\amd64_microsoft-windows-s..ssmanager.resources_31bf3856ad364e35_6.1.7600.16385_en-us_df658d4857ad8da5
1,C:\Python27\Lib\json\tests
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.VisualStudio.DataDesign.WpfDataTool\v4.0_10.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_wiaca00c.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2a6c49c557aaa43a
1,C:\Windows\inf\IEM
2,C:\Windows\winsxs\x86_microsoft-windows-w..ywmdmshellextension_31bf3856ad364e35_6.1.7601.17514_none_8ff5b6498cc24750
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_46\grep\share\locale\el\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\napsnap\a015e4dd451330be62225abb563d0de0
2,C:\Windows\winsxs\msil_microsoft.certificateservices.common_31bf3856ad364e35_6.1.7600.16385_none_806221b8143468d9
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.ManagedConnections\v4.0_11.0.0.0__89845dcd8080cc91
2,C:\Windows\System32\config\systemprofile\AppData\LocalLow
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.S01b51732#\c912998df34aa3f47d20a058bd34d099
2,C:\Windows\winsxs\x86_microsoft-windows-i..er-engine.resources_31bf3856ad364e35_6.1.7601.17514_sv-se_2e455c2305308809
1,C:\Windows\winsxs\x86_microsoft.windows.common-controls_6595b64144ccf1df_5.82.7601.18201_none_ec80f00e8593ece5
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\WindowsBase
2,C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft
2,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_it-it_e4c79be92250cb6e
2,C:\Windows\winsxs\amd64_microsoft-windows-nfs-openportmapper_31bf3856ad364e35_6.1.7601.17514_none_920a130a60c213ff
2,C:\Windows\winsxs\wow64_microsoft-windows-security-kerberos_31bf3856ad364e35_6.1.7601.17514_none_4f518cecfbcddc34
1,C:\Program Files\Microsoft SQL Server\110\Setup Bootstrap\SQLServer2012\1040_ITA_LP\x64\1040\help
2,C:\Windows\assembly\GAC_MSIL\Microsoft.Security.ApplicationId.Wizards.AutomaticRuleGenerationWizard
2,C:\Windows\winsxs\amd64_microsoft-windows-ie-imagesupport_31bf3856ad364e35_8.0.7600.16385_none_b4a401b283c17ad1
2,C:\Windows\winsxs\amd64_tsprint.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_94fa9583519bc058
2,C:\Windows\System32\en-US\Licenses\OEM\ServerSBSStandard
2,C:\Windows\assembly\GAC_MSIL\EventViewer.Resources\6.1.0.0_en_31bf3856ad364e35
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_71\grep\share\locale\pt_BR\LC_MESSAGES
2,C:\Users\Jim Olsen\Recent
2,C:\Windows\winsxs\amd64_microsoft-windows-s..lders-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_306353129db95bdd
2,C:\Windows\assembly\GAC_MSIL\System.DirectoryServices.Protocols\2.0.0.0__b03f5f7f11d50a3a
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_196\grep\share
1,C:\Windows\winsxs\amd64_netrndis.inf_31bf3856ad364e35_6.1.7601.17887_none_259febb55ca2345a
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Security.#\1966e104b20c7ee0537ec94244c6eb05
2,C:\Windows\winsxs\amd64_networking-mpssvc.resources_31bf3856ad364e35_6.1.7600.16385_en-us_24b3cfe4ff928bea
2,C:\Windows\winsxs\wow64_microsoft-windows-p..ll-events.resources_31bf3856ad364e35_6.1.7600.16385_en-us_493296f9a8635002
2,C:\Windows\winsxs\amd64_microsoft-windows-d..-charcodedictionary_31bf3856ad364e35_6.1.7600.16385_none_8555c0891265db3e
2,C:\Windows\winsxs\x86_microsoft-windows-i..tional-codepage-500_31bf3856ad364e35_6.1.7600.16385_none_ceda0134fc71635e
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.ServiceModel.Channels\v4.0_4.0.0.0__31bf3856ad364e35
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\SqlWorkbenchProjectItems\Sql\Audit
2,C:\Windows\System32\en-US\Licenses\eval\ServerWinSBV
2,C:\Windows\winsxs\x86_wpf-presentationframework.luna_31bf3856ad364e35_6.1.7601.17514_none_33660260677d7e6a
2,C:\Windows\winsxs\wow64_microsoft-windows-com-complus-admin_31bf3856ad364e35_6.1.7600.16385_none_43b350887adefc43
2,C:\Windows\winsxs\amd64_microsoft-windows-dims-autoenroll_31bf3856ad364e35_6.1.7600.16385_none_5004a8665487390e
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.Web\da5da08245467818759aa44c4eb948e1
1,C:\Windows\winsxs\wow64_microsoft-windows-uianimation.resources_31bf3856ad364e35_7.1.7601.16492_es-es_30e64d79b18289db
2,C:\Windows\winsxs\amd64_microsoft-windows-g..me-snapin.resources_31bf3856ad364e35_6.1.7600.16385_en-us_4753f21e9fa662df
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.D09177692#
1,C:\Windows\SoftwareDistribution\PostRebootEventCache
1,C:\Windows\winsxs\x86_microsoft-windows-xmllite_31bf3856ad364e35_6.1.7601.17633_none_8b2c4a4201a1c2f4
1,C:\Program Files\Common Files\Microsoft Shared\VS7Debug
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\SqlWorkbenchProjectItems\Sql\SQL Azure Database\Trigger
2,C:\Windows\winsxs\amd64_microsoft-windows-ie-jscriptdebugui_31bf3856ad364e35_8.0.7601.17514_none_334c9b845b46bf8d
2,C:\Windows\winsxs\amd64_ql40xx.inf_31bf3856ad364e35_6.1.7600.16385_none_574ac369ea0b9135
2,C:\Windows\winsxs\x86_microsoft-windows-n..ion-agent.resources_31bf3856ad364e35_6.1.7600.16385_en-us_15bf7202267cb05f
2,C:\Windows\System32\DriverStore\FileRepository\netxex64.inf_amd64_neutral_77b02fd738dca150
1,C:\Windows\winsxs\amd64_netfx-system_tlb_b03f5f7f11d50a3a_6.1.7601.22740_none_4871ba84575f992c
2,C:\Windows\winsxs\wow64_microsoft-windows-webio_31bf3856ad364e35_6.1.7601.17514_none_c564e9df29b386b8
2,C:\Windows\winsxs\wow64_microsoft-windows-migrationengine_31bf3856ad364e35_6.1.7601.17514_none_c122877426404910
2,C:\Windows\winsxs\amd64_microsoft-windows-b..dlinetool.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7d02b5319200e88c
2,C:\Windows\winsxs\amd64_microsoft-windows-nwifi.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6e0ae8581c7910f9
2,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-0001045d_31bf3856ad364e35_6.1.7600.16385_none_0747808f9651066f
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.WebServiceTaskUI
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_198\grep\share\locale\lt\LC_MESSAGES
2,C:\Windows\winsxs\wow64_microsoft-windows-taskscheduler-service_31bf3856ad364e35_6.1.7601.17514_none_977bce52e202c4f4
2,C:\Windows\winsxs\x86_addinprocess32_b77a5c561934e089_6.1.7601.17514_none_83171a284b28fcec
2,C:\Windows\winsxs\amd64_netl260a.inf_31bf3856ad364e35_6.1.7600.16385_none_d603843483dfa9aa
2,C:\Windows\winsxs\amd64_microsoft-windows-ie-hotmailapi_31bf3856ad364e35_6.1.7600.16385_none_c640cdfa5e9e8384
2,C:\Windows\winsxs\amd64_microsoft-windows-w..edtracing.resources_31bf3856ad364e35_6.1.7600.16385_en-us_1b774243b18f0918
2,C:\Windows\winsxs\amd64_microsoft-windows-crypt32-dll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2a1bcf35d3f77b46
2,C:\Windows\winsxs\msil_microsoft.virtualiz..ent.rdpclientaxhost_31bf3856ad364e35_6.1.7600.16385_none_a718774ed6eab4b1
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_113\grep\share\locale\pl\LC_MESSAGES
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.CustomControls.resources\11.0.0.0_fr_89845dcd8080cc91
1,C:\Program Files\Tanium\Tanium Server\Apache24\manual\style
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.MSMQTask
1,C:\Windows\winsxs\x86_microsoft-windows-m..cursor-library-ansi_31bf3856ad364e35_6.1.7601.21747_none_50bddeac182a2738
2,C:\Windows\winsxs\amd64_microsoft-windows-c..rtadm-dll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c2e353c5eb005391
2,C:\Windows\System32\en-US\Licenses\_Default\ServerSolutionsPremium
2,C:\Windows\winsxs\amd64_microsoft-windows-cdosys.resources_31bf3856ad364e35_6.1.7601.17514_he-il_a5134adfb1f79c3a
2,C:\Windows\SysWOW64\drivers\en-US
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_48\grep\share\locale\ga\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00020437_31bf3856ad364e35_6.1.7600.16385_none_8c1c84c0615562b0
1,C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE\CommonExtensions\Platform\NavigateTo\FileProvider
2,C:\Windows\winsxs\amd64_microsoft-windows-f..toragereportservice_31bf3856ad364e35_6.1.7601.17514_none_88d677c4cbf02778
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_191\grep\share\locale\rw\LC_MESSAGES
2,C:\Windows\diagnostics
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_106\grep\share\locale\fr\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_194\grep\contrib\grep
2,C:\Windows\winsxs\amd64_microsoft-windows-ocsetup_31bf3856ad364e35_6.1.7601.17514_none_41a3376575e751b4
2,C:\Windows\winsxs\amd64_server-help-h1s.dfs2_lh.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5e44ab16f4bd545b
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.Xml.Linq\3063abda312516739bc808360071bad9
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\PresentationFramewo#\f7fd822d5eda18da4ad1095020b42963
2,C:\Windows\System32\DriverStore\FileRepository\mdmnttme.inf_amd64_neutral_ece4b1cc5aee6a38
1,C:\Windows\winsxs\x86_microsoft-windows-os-kernel_31bf3856ad364e35_6.1.7601.18247_none_6e1a402c127aed77
2,C:\Windows\winsxs\msil_microsoft.windows.s..migration.downlevel_31bf3856ad364e35_6.1.7601.17514_none_acc3cb32fb786780
2,C:\Windows\winsxs\amd64_microsoft.windows.d..eshootingpackmodule_31bf3856ad364e35_6.1.7600.16385_none_7d19911b0fafbb5f
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_35\grep\share\locale\ko\LC_MESSAGES
2,C:\Windows\winsxs\amd64_iirsp.inf_31bf3856ad364e35_6.1.7600.16385_none_02496439a3048835
2,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\sv\LC_MESSAGES
1,C:\Windows\winsxs\x86_microsoft-windows-i..tocolimplementation_31bf3856ad364e35_11.2.9600.17358_none_882f3db7fe78ff91
2,C:\Windows\winsxs\amd64_wiahp001.inf_31bf3856ad364e35_6.1.7600.16385_none_ebc6374fdcadec8c
2,C:\Windows\winsxs\msil_microsoft.web.secur..gement.ws.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c8db2fb334b222ab
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_113\grep\share\locale\nl\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-d..-adamsync.resources_31bf3856ad364e35_6.1.7601.17514_en-us_fc7c0416355056ab
2,C:\Windows\winsxs\amd64_netfx-sys_data_oraclient_perfcoun_b03f5f7f11d50a3a_6.1.7600.16385_none_12b230ea15a9e57a
1,C:\Users\Jim Olsen\AppData\Local\Google\Chrome\User Data\Default\Storage\ext\chrome-signin\def
2,C:\Windows\winsxs\amd64_prnts002.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_06c0629adda1a73f
1,C:\Python27\tcl\tcl8.5\tzdata\Brazil
2,C:\Windows\winsxs\amd64_microsoft-windows-media-mp3acm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_872be93eaa9f6a40
2,C:\Windows\winsxs\x86_microsoft-windows-m..s-mdac-odbc-cpxl437_31bf3856ad364e35_6.1.7600.16385_none_5d617cc7e53174c0
2,C:\Windows\winsxs\x86_microsoft-windows-m..uxiliarydisplay-api_31bf3856ad364e35_6.1.7600.16385_none_f87a6669d7d0ab48
2,C:\Windows\winsxs\amd64_microsoft-windows-r..licensing-component_31bf3856ad364e35_6.1.7601.17514_none_fd3debee02c1ae74
1,C:\Program Files (x86)\Microsoft SQL Server\90
2,C:\Windows\winsxs\msil_system.web.routing_31bf3856ad364e35_6.1.7601.17514_none_1a58be6d26032dfe
1,C:\Program Files (x86)\Microsoft SQL Server\80
2,C:\Windows\winsxs\amd64_microsoft-windows-security-schannel-mof_31bf3856ad364e35_6.1.7600.16385_none_41b1a1917f0b6acd
2,C:\Windows\winsxs\wow64_microsoft-windows-audio-audiocore_31bf3856ad364e35_6.1.7601.17514_none_df1a73e82fa00c16
1,C:\Windows\winsxs\amd64_netfx-system.directoryservices_b03f5f7f11d50a3a_6.1.7601.22126_none_ffe9f729ba3ac93e
1,C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_26\grep\share\locale\pt\LC_MESSAGES
2,C:\Windows\winsxs\amd64_netfx-mscorwks_dll_b03f5f7f11d50a3a_6.1.7601.17514_none_bf0c7965d70a0677
1,C:\Windows\winsxs\amd64_microsoft-windows-b..os-loader.resources_31bf3856ad364e35_6.1.7601.22736_en-us_d534a81a13cf81d6
2,C:\Windows\winsxs\msil_napinit_31bf3856ad364e35_6.1.7600.16385_none_0c1c21010a6f7ac2
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.DataTransformationServices.Controls\v4.0_11.0.0.0__89845dcd8080cc91
2,C:\Windows\inf\TermService\0409
2,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Messaging
1,C:\Windows\winsxs\amd64_microsoft-windows-d2d.resources_31bf3856ad364e35_7.1.7601.16492_pt-pt_e93415d358c6c7f8
2,C:\Windows\winsxs\msil_aagmmc_31bf3856ad364e35_6.1.7601.17514_none_898dc291b8e98573
2,C:\Windows\winsxs\amd64_microsoft-windows-adfs-webagentclaims_31bf3856ad364e35_6.1.7600.16385_none_b1d49ce86105b3b0
2,C:\Windows\winsxs\amd64_server-help-chm.tpmadmin.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f4a21ac6fd93957d
2,C:\Windows\winsxs\amd64_microsoft-windows-font-truetype-miriam_31bf3856ad364e35_6.1.7600.16385_none_7b7a9e11df9f30a1
1,C:\Windows\assembly\GAC_MSIL\Microsoft.ReportViewer.WebForms.resources
2,C:\Windows\winsxs\x86_microsoft-windows-muicachebuilder_31bf3856ad364e35_6.1.7601.17514_none_1c140627131a6df3
2,C:\Windows\winsxs\x86_microsoft-windows-i..er-engine.resources_31bf3856ad364e35_6.1.7601.17514_sl-si_3077981303bb82bb
1,C:\Windows\winsxs\amd64_microsoft-windows-errorreportingcore_31bf3856ad364e35_6.1.7601.22584_none_7eda8c2e35da4605
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_18\grep\share\locale\da\LC_MESSAGES
1,C:\Users\Jim Olsen\AppData\Local\Microsoft\Internet Explorer\IECompatData
1,C:\Windows\winsxs\wow64_microsoft-windows-i..etexplorer-optional_31bf3856ad364e35_11.2.9600.17041_none_858ffb5bf711c81f
2,C:\Windows\winsxs\amd64_microsoft-windows-a..ility-assistant-adm_31bf3856ad364e35_6.1.7600.16385_none_7b487ca06770a648
2,C:\Windows\winsxs\amd64_microsoft-windows-mlang.resources_31bf3856ad364e35_6.1.7600.16385_zh-hk_4068f777147d0327
2,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-0000045a_31bf3856ad364e35_6.1.7600.16385_none_587ffcaa703a19a6
2,C:\Windows\winsxs\msil_microsoft.security...agement.policymodel_31bf3856ad364e35_6.1.7600.16385_none_a590f64d5cfc5ee6
2,C:\Windows\winsxs\amd64_server-help-h1s.ts_workspace.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5ac6cdee8e955606
1,C:\Windows\winsxs\msil_smsvchost_b03f5f7f11d50a3a_6.1.7601.22743_none_cfeb95652ab9a380
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_119\grep\share\locale\sk\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-f12-provider_31bf3856ad364e35_11.2.9600.17420_none_bd94efe47e8cda1f
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_195\grep\share\locale\et\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-l..verwinsbv.resources_31bf3856ad364e35_6.1.7600.16385_en-us_123629cbcb3c1d84
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Comp7dda8007#\4b684fa1cf890ed47d5a722193b11d37
2,C:\Windows\SysWOW64\en-US\Licenses\_Default\ServerStorageEnterprise
2,C:\Windows\winsxs\x86_microsoft-windows-m..server-provider-rll_31bf3856ad364e35_6.1.7600.16385_none_64ce4cfce74e3347
2,C:\Windows\winsxs\x86_microsoft-windows-photoviewer.resources_31bf3856ad364e35_6.1.7600.16385_en-us_1f351a21979e0848
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_195\grep\share\locale\nl\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-n..n_service_licensing_31bf3856ad364e35_6.1.7600.16385_none_6e4d66798d098a3d
2,C:\Windows\winsxs\amd64_microsoft-windows-b..nager-efi.resources_31bf3856ad364e35_6.1.7600.16385_zh-tw_3e4f8e47e730ab98
1,C:\Windows\assembly\GAC_MSIL\Microsoft.Web.Administration\7.0.0.0__31bf3856ad364e35
1,C:\Windows\winsxs\x86_netfx-aspnet_wp_exe_b03f5f7f11d50a3a_6.1.7601.18205_none_99441e0948ed8ae7
2,C:\Windows\winsxs\amd64_microsoft-windows-msxml30_31bf3856ad364e35_6.1.7601.17514_none_e6944609ad75ac7d
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Templates
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_37\grep\share\locale\nl\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_108\grep\share\locale\fi\LC_MESSAGES
1,C:\Windows\winsxs\wow64_microsoft-windows-i..etexplorer-optional_31bf3856ad364e35_11.2.9600.17358_none_856fec69f729e8b0
2,C:\Windows\winsxs\x86_microsoft-windows-l..gementsvc.resources_31bf3856ad364e35_6.1.7600.16385_en-us_bdce5e8f2057dbf5
2,C:\Windows\winsxs\amd64_microsoft-windows-qos.resources_31bf3856ad364e35_6.1.7600.16385_en-us_97579d95c8092c0f
2,C:\Windows\winsxs\amd64_microsoft-windows-g..-computer.resources_31bf3856ad364e35_6.1.7601.17514_en-us_b08d7490ca2188cd
2,C:\Windows\winsxs\x86_microsoft-windows-fdeploy.resources_31bf3856ad364e35_6.1.7600.16385_en-us_0d70be959d80ac53
2,C:\Windows\winsxs\amd64_microsoft-windows-fax-service.resources_31bf3856ad364e35_6.1.7600.16385_en-us_36e0de390f55ac1d
1,C:\Windows\winsxs\msil_system.data.sqlxml_b77a5c561934e089_6.1.7601.18529_none_05d526a261a2bd9d
2,C:\Windows\winsxs\msil_microsoft.visualbasic.compatibility_b03f5f7f11d50a3a_6.1.7601.17514_none_c1c1077951dca19a
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_35\grep\share\locale\fr\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\Microsoft.S6a1f6e12#\f400877b07f0bce50e102093835631b4
2,C:\Windows\assembly\GAC_MSIL\napsnap
2,C:\Users\Default\AppData\Roaming\Microsoft
2,C:\Windows\Downloaded Program Files
2,C:\Windows\winsxs\x86_microsoft-windows-d..g-adminui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b82c74eec637335f
1,C:\Windows\Installer\{BED1EA3D-592D-4305-9D1F-20F03726EFC1}
2,C:\Windows\System32\en-US\Licenses\eval\ServerEssentialAdditional
1,C:\Windows\winsxs\wow64_microsoft-windows-ie-ieetwcollector_31bf3856ad364e35_11.2.9600.17239_none_afd8df784c24b3b6
2,C:\Windows\winsxs\x86_microsoft-windows-m..onents-mdac-odbcbcp_31bf3856ad364e35_6.1.7600.16385_none_b0d14a16af76d049
1,C:\Windows\winsxs\x86_microsoft-windows-ncrypt-dll_31bf3856ad364e35_6.1.7601.22010_none_606b38f468ff8cd3
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\yara
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_122\grep\share\locale\ja\LC_MESSAGES
2,C:\Windows\winsxs\amd64_mdmpace.inf_31bf3856ad364e35_6.1.7600.16385_none_1fe2fc8d4a1d4f7d
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Data.Linq\d8ac424adb7b7b4483bcf3aacb595ddf
2,C:\Windows\winsxs\amd64_microsoft-windows-w..-provider.resources_31bf3856ad364e35_6.1.7600.16385_en-us_572656a8a53c6a63
2,C:\Windows\winsxs\amd64_microsoft-windows-com-dtc-tracing_31bf3856ad364e35_6.1.7600.16385_none_73d43c6a0c805ae7
2,C:\Windows\winsxs\x86_microsoft-windows-basedependencies_31bf3856ad364e35_6.1.7600.16385_none_027847e78a22fdb1
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Xaml\v4.0_4.0.0.0__b77a5c561934e089
2,C:\Windows\winsxs\x86_microsoft-windows-l2na.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a62167de39951d5f
2,C:\Windows\winsxs\amd64_scsidev.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_de2a981bd7e66585
2,C:\Windows\winsxs\amd64_microsoft-windows-d..iagnostic.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ddf81a85f99d6d20
2,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_sk-sk_ea3f9509df3aaa93
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.Vd5001c35#\84eeb098e86a18b2dbf471975427083b
1,C:\Windows\winsxs\x86_microsoft-windows-ie-controls.resources_31bf3856ad364e35_11.2.9600.16428_en-us_34218f701493f41c
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\schemas\sqlserver\2004\SOAP\types\SqlResultStream
2,C:\Windows\winsxs\x86_microsoft-windows-s..-binaries.resources_31bf3856ad364e35_6.1.7601.17514_bg-bg_68d21d71f179ba4c
1,C:\Windows\winsxs\wow64_microsoft-windows-ie-htmlrendering_31bf3856ad364e35_8.0.7601.18571_none_96341266e45f3517
1,C:\Windows\winsxs\x86_microsoft-windows-i..rityzones.resources_31bf3856ad364e35_11.2.9600.17239_en-us_f4d1b46a3e1920f7
2,C:\Windows\winsxs\x86_microsoft-windows-t..ager-snapin-nonmsil_31bf3856ad364e35_6.1.7601.17514_none_8ddf701800eea858
1,C:\Windows\winsxs\amd64_wcf-system.servicemodel.washosting_b03f5f7f11d50a3a_6.1.7601.22733_none_eb759ec5609ff00b
1,C:\Windows\winsxs\amd64_microsoft-windows-b..gertransport-serial_31bf3856ad364e35_6.1.7601.21655_none_703aeff2dc87a23b
1,C:\Windows\winsxs\amd64_microsoft-windows-f..vices-bpa.resources_31bf3856ad364e35_7.1.7600.16422_en-us_badf5eb9b8b2a0e3
1,C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ASP.NETWebAdminFiles\AppConfig\App_LocalResources
2,C:\Users\All Users\Microsoft\Vault
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.V969c9247#
2,C:\Users\Default\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
2,C:\Windows\winsxs\x86_microsoft-windows-d..ing-management-core_31bf3856ad364e35_6.1.7601.17514_none_2d3b8ff08901343f
2,C:\Windows\System32\DriverStore\FileRepository\prnsa002.inf_amd64_neutral_d9df1d04d8cbe336\Amd64
1,C:\Windows\winsxs\x86_microsoft-windows-p..age-codec.resources_31bf3856ad364e35_7.1.7601.16492_hu-hu_8c9313d3f0035f71
2,C:\Windows\winsxs\amd64_microsoft-windows-com-dtc-client_31bf3856ad364e35_6.1.7600.16385_none_a8e7df5dd2fecf4e
2,C:\Windows\System32\DriverStore\FileRepository\netb57va.inf_amd64_neutral_6264e97d4fc12211
1,C:\Windows\winsxs\x86_microsoft-windows-c..ityclient.resources_31bf3856ad364e35_6.1.7601.22705_en-us_675c18f5172b8636
2,C:\Windows\assembly\GAC_MSIL\Microsoft.Windows.Diagnosis.TroubleshootingPack\6.1.0.0__31bf3856ad364e35
2,C:\Windows\winsxs\amd64_microsoft-windows-ndisuio_31bf3856ad364e35_6.1.7601.17514_none_ca170d32fd7da822
2,C:\Windows\winsxs\amd64_microsoft-windows-t..tkeyboard.resources_31bf3856ad364e35_6.1.7600.16385_en-us_441e533e5fd46b57
2,C:\Windows\winsxs\amd64_microsoft-windows-ie-ratings.resources_31bf3856ad364e35_8.0.7600.16385_en-us_d06c65741a79bece
1,C:\Windows\winsxs\amd64_microsoft-windows-kernel32.resources_31bf3856ad364e35_6.1.7601.22125_en-us_9bc075d0550900c8
2,C:\Windows\winsxs\amd64_netg664.inf_31bf3856ad364e35_6.1.7600.16385_none_3e838f62f7e92ab2
1,C:\Windows\winsxs\amd64_microsoft-windows-tcpip-adm.resources_31bf3856ad364e35_6.1.7601.22124_en-us_35aca0a73d918fae
2,C:\Windows\assembly\GAC_MSIL\Microsoft.Windows.Diagnosis.TroubleshootingPack.Resources\6.1.0.0_en_31bf3856ad364e35
2,C:\Windows\winsxs\amd64_wcf-m_svc_mod_op_perf_c_reg_31bf3856ad364e35_6.1.7600.16385_none_23b47b1a46320a55
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\UIAutomationClient
2,C:\Windows\winsxs\amd64_netbvbda.inf_31bf3856ad364e35_6.1.7600.16385_none_fa388bc43a1db8d8
2,C:\Windows\winsxs\amd64_netfx-vb_compiler_ui_b03f5f7f11d50a3a_6.1.7600.16385_none_281aa88152564d62
2,C:\Windows\winsxs\x86_netfx35linq-system.core_31bf3856ad364e35_6.1.7601.17514_none_6161fc35ed136622
2,C:\Windows\winsxs\amd64_microsoft-windows-blb-engine-main_31bf3856ad364e35_6.1.7601.17514_none_4207fb67165f731a
2,C:\Windows\winsxs\amd64_microsoft.windows.s..ermanager.resources_31bf3856ad364e35_6.1.7601.17514_en-us_acfc1bedef374d3e
1,C:\Windows\assembly\GAC_MSIL\Microsoft.VisualStudio.TextManager.Interop.10.0\10.0.0.0__b03f5f7f11d50a3a
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\Microsoft.Seae4f488#
1,C:\Python27\Lib\json
1,C:\Windows\winsxs\amd64_wcf-system.servicemodel_b03f5f7f11d50a3a_6.1.7601.18532_none_a1aa0c9e9399ac00
2,C:\Users\Jim Olsen\AppData\Local
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_18\grep\man
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Dynamic.Runtime\v4.0_4.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_microsoft-windows-s..llercommandlinetool_31bf3856ad364e35_6.1.7600.16385_none_d0632cbfee5db937
2,C:\Windows\winsxs\amd64_microsoft-windows-dns-client-winrnr_31bf3856ad364e35_6.1.7600.16385_none_b543449669c73e11
2,C:\Windows\winsxs\amd64_tpm.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5cf8a45092f4398d
2,C:\Windows\winsxs\x86_netfx35linq-microso..ild.conversion.v3.5_31bf3856ad364e35_6.1.7600.16385_none_397c457d247d92a0
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Windows.Pres#
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.V78b5b27e#\5a605232baa4a7d29ba3132780da8388
2,C:\Windows\winsxs\x86_microsoft-windows-t..vices-configbackend_31bf3856ad364e35_6.1.7600.16385_none_d66b4dbb52eb8cae
2,C:\Windows\winsxs\x86_microsoft-windows-i..nal-nlsdownleveldll_31bf3856ad364e35_6.1.7600.16385_none_087f597fb956baeb
2,C:\Windows\winsxs\amd64_microsoft-windows-a..rvice-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_68408642f41ba602
1,C:\Windows\winsxs\x86_netfx-_vc_assembly_linker_messages_b03f5f7f11d50a3a_6.1.7601.18523_none_398e4a7961a6d332
2,C:\Windows\winsxs\amd64_microsoft-windows-w..eakerstemmer-korean_31bf3856ad364e35_7.0.7600.16385_none_a7ca197ff4659c3d
1,C:\Program Files\Tanium\Tanium Server\Apache24\htdocs\console\history
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_37\grep\share\locale\ko\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-smss_31bf3856ad364e35_6.1.7601.22411_none_0ae72ec548f19d13
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.Management.MultiServerConnection
1,C:\Windows\winsxs\msil_smdiagnostics_b77a5c561934e089_6.1.7601.18532_none_72f0e00b6ca38779
1,C:\Windows\winsxs\wow64_microsoft-windows-ie-sysprep_31bf3856ad364e35_11.2.9600.16428_none_083dd731036b79d4
2,C:\Windows\winsxs\amd64_microsoft-windows-i..trolpanel.resources_31bf3856ad364e35_8.0.7601.17514_en-us_9b6af1fe75cda5cc
2,C:\Windows\SysWOW64\config\systemprofile\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\A5OS7C95
2,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\ca\LC_MESSAGES
1,C:\Windows\winsxs\x86_microsoft-windows-c..tionauthorityclient_31bf3856ad364e35_6.1.7601.22653_none_d9e26570b428b109
1,C:\Windows\assembly\GAC_MSIL\System.Windows.Presentation
2,C:\Windows\winsxs\amd64_microsoft-windows-l..geexpress.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f9a5260e9a61f34a
2,C:\Windows\winsxs\amd64_mdmbr007.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_186c2c8ed691aa61
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_194\grep\share\locale\ja\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Design\d42a48a3e73b472a80d0d44038af89b0
1,C:\Windows\winsxs\amd64_microsoft-windows-advapi32_31bf3856ad364e35_6.1.7601.22436_none_41e43a0cb64d6c9e
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_18\grep\share\locale\ru\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-c..complus-runtime-qfe_31bf3856ad364e35_6.1.7600.16385_none_c7582028923fd980
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_106\grep\share\locale\af\LC_MESSAGES
1,C:\Windows\winsxs\x86_microsoft-windows-security-credssp_31bf3856ad364e35_6.1.7601.22865_none_c61415d8191776a1
2,C:\Windows\winsxs\x86_microsoft-windows-d..ervicing-management_31bf3856ad364e35_6.1.7600.16385_none_5e7ff93b6f0000b7
2,C:\Windows\System32\WindowsPowerShell\v1.0\Modules
2,C:\Windows\diagnostics\system\PCW\en-US
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.Ddc0c32eb#
1,C:\Windows\winsxs\amd64_microsoft-windows-shdocvw.resources_31bf3856ad364e35_6.1.7601.22403_en-us_267c18cf89f1b2b9
2,C:\Windows\winsxs\amd64_microsoft-windows-a..es-interface-router_31bf3856ad364e35_6.1.7600.16385_none_b3eaf84f983a33ee
2,C:\Windows\winsxs\amd64_microsoft-hyper-v-clustering-vmclusex_31bf3856ad364e35_6.1.7600.16385_none_7269d6cc3517cad1
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.S2712f5ba#
1,C:\Windows\winsxs\amd64_microsoft-windows-g..validatefntcache-03_31bf3856ad364e35_6.1.7600.21258_none_a56ffdd44d4053c0
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\SrpUxSnapIn\ed407e1bee9113f340584de83ad7692c
2,C:\Windows\winsxs\x86_wpf-uiautomationclientsideproviders_31bf3856ad364e35_6.1.7600.16385_none_54926688afb9f1e9
2,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.Runtime.Remo#
2,C:\Windows\winsxs\msil_microsoft.bestpractices_31bf3856ad364e35_6.1.7600.16385_none_900eab16ba805783
2,C:\Windows\System32\DriverStore\FileRepository\tsusbhubfilter.inf_amd64_neutral_d0615d6fd67bad03
2,C:\Windows\winsxs\x86_microsoft-windows-d..computers.resources_31bf3856ad364e35_6.1.7601.17514_en-us_8f1f3a4e13edfb30
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.VisualStudio.Editors\v4.0_10.0.0.0__b03f5f7f11d50a3a
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.Sae9b8ed1#
2,C:\Windows\winsxs\x86_microsoft-windows-i..er-engine.resources_31bf3856ad364e35_6.1.7601.17514_pl-pl_4871a5da2b2cebc2
2,C:\Windows\winsxs\amd64_microsoft-windows-sud_31bf3856ad364e35_6.1.7601.17514_none_05cbfa317289b4af
2,C:\Windows\winsxs\amd64_microsoft-windows-registry-editor_31bf3856ad364e35_6.1.7600.16385_none_5023a70bf589ad3e
2,C:\Windows\winsxs\amd64_ql40xx.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d3a27a362b551c07
2,C:\Windows\winsxs\x86_microsoft-windows-d..ommandline-redirect_31bf3856ad364e35_6.1.7600.16385_none_2d3a368613e27ef0
2,C:\Windows\winsxs\x86_microsoft-windows-video-for-windows16_31bf3856ad364e35_6.1.7600.16385_none_5fd0557cd88ef5bd
1,C:\Windows\winsxs\x86_microsoft-windows-d..ices-boot-files-x64_31bf3856ad364e35_6.1.7601.22736_none_bea4c27935b328e9
2,C:\Windows\winsxs\amd64_microsoft-windows-i..ttpprotocolbinaries_31bf3856ad364e35_6.1.7600.16385_none_f5c9ab3453234070
1,C:\Windows\winsxs\amd64_microsoft-windows-ocspsvc.resources_31bf3856ad364e35_6.1.7601.22712_en-us_b37fd6fae5a1ce7d
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.VisualStudio.Platform.VSEditor\v4.0_10.0.0.0__b03f5f7f11d50a3a
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\SqlWorkbenchProjectItems\Sql\Database
1,C:\Windows\System32\DriverStore\FileRepository\mshdc.inf_amd64_neutral_552ea5111ec825a6
1,C:\Users\Jim Olsen\AppData\Local\Microsoft\Internet Explorer\VersionManager
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\SqlWorkbenchProjectItems\Sql\Function
2,C:\Windows\winsxs\x86_system.web.security..non.claimtransforms_31bf3856ad364e35_6.1.7600.16385_none_653a2bcb369d63be
1,C:\Windows\winsxs\x86_microsoft-windows-w..-infrastructure-bsp_31bf3856ad364e35_6.1.7601.18254_none_ba2f64c78bae6989
2,C:\Windows\winsxs\x86_microsoft-windows-cdosys.resources_31bf3856ad364e35_6.1.7601.17514_sv-se_476e370068602811
2,C:\Windows\winsxs\amd64_microsoft-windows-m..ow-gadget.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e45ff59acede6483
1,C:\Windows\winsxs\x86_presentationcore_31bf3856ad364e35_6.1.7601.17755_none_ae0e4090ee55e5f0
2,C:\Windows\winsxs\amd64_microsoft-windows-d..aanalyzer.resources_31bf3856ad364e35_6.1.7601.17514_en-us_81c4acf1faf29d3d
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_102\grep\share\locale
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Data.DataSetExtensions
1,C:\Windows\winsxs\wow64_microsoft-windows-coreos_31bf3856ad364e35_6.1.7601.18288_none_8d852b428986de92
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_51\grep\manifest
2,C:\Windows\winsxs\x86_wpf-presentationcffrasterizernative_31bf3856ad364e35_6.1.7600.16385_none_c96bb53eefa606a7
2,C:\Windows\winsxs\x86_microsoft-windows-setx_31bf3856ad364e35_6.1.7600.16385_none_ac4d2bf27a63f85f
2,C:\Windows\winsxs\amd64_microsoft-windows-ie-antiphishfilter_31bf3856ad364e35_8.0.7600.16385_none_72414f35fc718b5d
2,C:\Windows\winsxs\wow64_microsoft-windows-i..stfilteringbinaries_31bf3856ad364e35_6.1.7600.16385_none_38daa6d0fa5c3fac
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.VisualStudio.TextTemplating.Modeling.10.0\v4.0_10.0.0.0__b03f5f7f11d50a3a
1,C:\Users\Jim Olsen\AppData\Local\Google\Chrome\User Data\Default\Extensions\aohghmighlieiainnegkcijnfilokake\0.7_0\_locales\en_US
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_188\grep\share\locale\bg\LC_MESSAGES
1,C:\Windows\winsxs\x86_netfx-web_engine_dll_b03f5f7f11d50a3a_6.1.7601.18410_none_0afbfa6df48eab41
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_52\grep\share\locale\bg\LC_MESSAGES
2,C:\Windows\winsxs\msil_microsoft.storage.sancommon.resources_31bf3856ad364e35_6.1.7601.17514_en-us_93efbccba2864c06
1,C:\Windows\winsxs\msil_system.runtime.remoting_b77a5c561934e089_6.1.7601.18410_none_99f1269f01d59174
2,C:\Windows\winsxs\amd64_microsoft-windows-wab-core.resources_31bf3856ad364e35_6.1.7600.16385_en-us_0c4d010cb13d4746
1,C:\Windows\winsxs\amd64_microsoft-windows-iologgingdll.resources_31bf3856ad364e35_6.1.7601.18386_en-us_52e76a5df068c2f9
2,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\sk\LC_MESSAGES
2,C:\Windows\winsxs\x86_microsoft-windows-advapi32_31bf3856ad364e35_6.1.7601.17514_none_e54fbb95e4c3d1bb
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-adminkitbranding_31bf3856ad364e35_11.2.9600.17280_none_56c3d9416c74f49a
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_102\grep\share\locale\fi\LC_MESSAGES
1,C:\Windows\winsxs\x86_netfx-shared_netfx_20_mscorwks_31bf3856ad364e35_6.1.7601.22724_none_8234995dbdb9c5f5
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\UIAutomatio4e153cb6#\d46a55d0e870a8ad2cb0b1d6d7b7f6e6
2,C:\Windows\winsxs\x86_microsoft-windows-l..nspremium.resources_31bf3856ad364e35_6.1.7600.16385_en-us_368ed530484c96ae
2,C:\Windows\winsxs\x86_microsoft-windows-console.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7df7d893a3a353f9
1,C:\Users\Jim Olsen\AppData\Local\Temp\nsg79B3.tmp
2,C:\Windows\winsxs\wow64_microsoft-windows-s..ty-protectedstorage_31bf3856ad364e35_6.1.7600.16385_none_ae92b0937e708d46
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_37\grep\share\locale\fr\LC_MESSAGES
2,C:\Windows\SysWOW64\en-US\Licenses\_Default\ServerWinFoundation
2,C:\Program Files\Common Files\VMware\Drivers\vmci\sockets\include
1,C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SetupCache
2,C:\Windows\System32\DriverStore\FileRepository\mshdc.inf_amd64_neutral_aad30bdeec04ea5e
1,C:\Windows\winsxs\x86_microsoft-windows-browserservice-netapi_31bf3856ad364e35_6.1.7601.17887_none_2f4c24e0f632f0d7
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_195\grep\contrib
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_71\yara
2,C:\Windows\winsxs\x86_microsoft-windows-lsa-msprivs.resources_31bf3856ad364e35_6.1.7600.16385_zh-cn_c6baef0e416653d3
2,C:\Users\Jim Olsen\Music
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-jscriptdebugui_31bf3856ad364e35_8.0.7601.18571_none_3308a4565b7a34cf
1,C:\Users\Jim Olsen\AppData\Local\Google\Chrome\User Data\Default\Extensions\aohghmighlieiainnegkcijnfilokake\0.7_0\_locales\en_GB
2,C:\Windows\winsxs\amd64_microsoft-windows-n.._service_runtimeapi_31bf3856ad364e35_6.1.7600.16385_none_e789f0e67a8cb67d
2,C:\Windows\winsxs\amd64_microsoft-windows-w..onservice.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f39c7dc580011c1c
2,C:\Windows\winsxs\x86_microsoft-windows-i..o4-codecs.resources_31bf3856ad364e35_6.1.7600.16385_en-us_fdd5773ab7f778a7
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_48\grep\share\locale\be\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-i..rityzones.resources_31bf3856ad364e35_11.2.9600.17041_en-us_5107a64ff664a69a
2,C:\Windows\winsxs\amd64_prnca00c.inf_31bf3856ad364e35_6.1.7600.16385_none_ddc7f96bf68e339f\Amd64
2,C:\Windows\winsxs\amd64_prnin003.inf_31bf3856ad364e35_6.1.7600.16385_none_11a5503ce5abb7ec
2,C:\Windows\winsxs\amd64_microsoft-windows-i..libraries.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ac2f25e3d4ed4318
2,C:\Windows\winsxs\amd64_microsoft-windows-help-sharing.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c09c55124df2c34c
2,C:\Windows\winsxs\x86_microsoft-windows-vssproxystub_31bf3856ad364e35_6.1.7600.16385_none_3092767d8b44f463
2,C:\Windows\winsxs\x86_microsoft-windows-dot3gpclient_31bf3856ad364e35_6.1.7600.16385_none_7a2a3d711dcb2bb3
2,C:\Windows\winsxs\amd64_microsoft-windows-s..ngine-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_92ae7bc7fccaab93
2,C:\Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\EnvDTE\e49bbbb530f07efcd89ea2e679fed2b3
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Dire573b08f5#
2,C:\Windows\winsxs\amd64_microsoft-windows-e..otocol-host-service_31bf3856ad364e35_6.1.7600.16385_none_e63ed98817cf16b1
2,C:\Windows\winsxs\amd64_microsoft-windows-help-ics.resources_31bf3856ad364e35_6.1.7600.16385_en-us_bd437fd8ba6789d7
2,C:\Windows\inf\StarterGPOs\{B52976F5-3EE4-4C77-80B9-11911F065EF7}\Machine
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_196\grep\share\locale\sr\LC_MESSAGES
1,C:\inetpub\history\CFGHISTORY_0000000002
1,C:\inetpub\history\CFGHISTORY_0000000003
1,C:\inetpub\history\CFGHISTORY_0000000001
1,C:\inetpub\history\CFGHISTORY_0000000006
1,C:\inetpub\history\CFGHISTORY_0000000004
1,C:\inetpub\history\CFGHISTORY_0000000005
2,C:\Windows\winsxs\amd64_microsoft-windows-securitycenter-adm_31bf3856ad364e35_6.1.7600.16385_none_423ff0e3a3f91a83
2,C:\Windows\winsxs\amd64_microsoft-windows-nap-oobshv_31bf3856ad364e35_6.1.7600.16385_none_efd6cac15d5cf99e
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\ComSvcConfig
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_194\grep\share\locale\uk\LC_MESSAGES
2,C:\Windows\winsxs\amd64_mstape.inf_31bf3856ad364e35_6.1.7600.16385_none_89fe250f2f057e08
2,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_de-de_677ec5ef54cba91e
2,C:\Windows\winsxs\amd64_tape.inf_31bf3856ad364e35_6.1.7600.16385_none_426fc940972f24c6
2,C:\Users\Jim Olsen\AppData\Local\Temporary Internet Files
1,C:\Windows\winsxs\amd64_microsoft-windows-dhcp-client-dll_31bf3856ad364e35_6.1.7601.22130_none_35f00a945e60f3e9
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Ente96d83b35#\c44702fea0bcbd8e4b3e930f1f5ec2b7
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\System.Serv14b62006#\50ad6d7905012a0b6803293630998352
2,C:\Windows\winsxs\amd64_megasas.inf_31bf3856ad364e35_6.1.7600.16385_none_8c3546e368634d85
2,C:\Windows\winsxs\x86_microsoft-windows-msmq-runtime_31bf3856ad364e35_6.1.7601.17514_none_a2e93e679472903c
2,C:\Windows\winsxs\amd64_microsoft-windows-dfsr-readonly_31bf3856ad364e35_6.1.7601.17514_none_adac10295a6399ef
2,C:\Windows\winsxs\x86_microsoft-windows-cdosys.resources_31bf3856ad364e35_6.1.7601.17514_de-de_b9615ede3154164a
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Reflection\v4.0_4.0.0.0__b03f5f7f11d50a3a
1,C:\Windows\winsxs\msil_microsoft.jscript_b03f5f7f11d50a3a_6.1.7601.22733_none_8fbdcd1c5957f508
1,C:\Program Files (x86)\Microsoft SQL Server\100\Shared
2,C:\Windows\assembly\GAC_32\System.Transactions
2,C:\Windows\winsxs\x86_microsoft-windows-m..s-components-jetole_31bf3856ad364e35_6.1.7600.16385_none_7726de8ef25840f2
2,C:\Windows\winsxs\wow64_microsoft-windows-pnpdevicemanager_31bf3856ad364e35_6.1.7600.16385_none_7a20366b6d92814f
2,C:\Windows\winsxs\amd64_microsoft-windows-sort_31bf3856ad364e35_6.1.7600.16385_none_07b314fa3333f10d
2,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\contrib\grep\2.5.4\grep-2.5.4-src\doc
1,C:\Windows\winsxs\amd64_microsoft-windows-i..timezones.resources_31bf3856ad364e35_6.1.7601.18588_en-us_e1539265989b5275
2,C:\Windows\winsxs\msil_microsoft.build.engine_b03f5f7f11d50a3a_6.1.7601.17514_none_0cfd67f8cb24384c
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\PresentationBuildTasks
2,C:\Windows\winsxs\x86_microsoft-windows-comctl32-v5.resources_31bf3856ad364e35_6.1.7600.16385_da-dk_bc83aeba06823a38
2,C:\Windows\winsxs\amd64_microsoft-windows-d..cking-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_817cd4dab042e1f5
2,C:\Windows\SysWOW64\migration\WSMT\rras\dlmanifests
1,C:\Windows\winsxs\amd64_microsoft-windows-a..ence-mitigations-c3_31bf3856ad364e35_6.1.7601.18076_none_6a0b3ef309192aee
2,C:\Program Files\Common Files\Microsoft Shared\ink\ar-SA
2,C:\Windows\System32\DriverStore\FileRepository\mdmgl001.inf_amd64_neutral_9209e816461a1a73
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_71\grep\share\locale\nl\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_63\grep\share\locale\hr\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-f12_31bf3856ad364e35_11.2.9600.17041_none_d0392feefd4e1c62
2,C:\Windows\assembly\NativeImages_v2.0.50727_64\SecurityAuditPolici#
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.GridControl.resources\11.0.0.0_ko_89845dcd8080cc91
2,C:\Windows\System32\DriverStore\FileRepository\hdaudio.inf_amd64_neutral_ce7bc199c85ae0a0
2,C:\Windows\winsxs\amd64_netfx-system.management_b03f5f7f11d50a3a_6.1.7601.17514_none_f6397b438cd5e46b
2,C:\Windows\winsxs\amd64_microsoft-windows-w..enger-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_eca185f03b488843
2,C:\Windows\winsxs\x86_microsoft-windows-m..ds-ce-rll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_0def3c4a82afa650
2,C:\Windows\winsxs\amd64_microsoft-windows-t..cheduler-apis-proxy_31bf3856ad364e35_6.1.7600.16385_none_31a8e7113546f43e
2,C:\Windows\inf\StarterGPOs\{9C03F88D-8608-44B7-A3E7-7316D1CAC152}
2,C:\Windows\winsxs\amd64_microsoft-windows-bcrypt-primitives-dll_31bf3856ad364e35_6.1.7601.17514_none_70577ed42da9d71d
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_71\grep\share\locale\pt_BR
2,C:\Windows\System32\DriverStore\FileRepository\prnep00c.inf_amd64_neutral_f0d9ddf52f04765c
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_47\grep\share\locale\be\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-o..s-service.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b478b9e3e9b9a4f4
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.V48e48ead#
2,C:\Windows\winsxs\wow64_windowssearchengine.resources_31bf3856ad364e35_7.0.7600.16385_en-us_1eb04467622ff377
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_23\grep\share\locale\es\LC_MESSAGES
1,C:\Python27\Lib\sqlite3\test
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\vi
2,C:\Windows\winsxs\x86_microsoft-windows-wdc-events_31bf3856ad364e35_6.1.7600.16385_none_d3d56c8ea90213c5
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\tr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\uk
2,C:\Windows\winsxs\amd64_microsoft-windows-b..vironment-os-loader_31bf3856ad364e35_6.1.7601.17514_none_b94cbfa183466a89
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ro
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ru
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\rw
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_48\grep\share\locale\af\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\sv
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\sr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\sl
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\sk
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\pl
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\pt
1,C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\SqlWorkbenchProjectItems\Sql\Recursive Queries
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\nb
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\nl
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_21\grep\contrib\grep\2.5.4\grep-2.5.4-src\vms
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\lt
2,C:\Windows\winsxs\amd64_netb57va.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_33385dd47fa88b38
2,C:\Windows\System32\DriverStore\FileRepository\netbc664.inf_amd64_neutral_673d3dfb961e9b17
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ja
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\System.Drawing
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_196\grep\contrib\grep\2.5.4\grep-2.5.4-src\bootstrap
2,C:\Windows\winsxs\wow64_microsoft-windows-powershell_31bf3856ad364e35_6.1.7601.17514_none_65ab62a5f1bba14b
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ko
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ky
1,C:\Windows\winsxs\amd64_netfx-dfdll_dll_b03f5f7f11d50a3a_6.1.7601.22794_none_fe39bfb4165583e2
2,C:\Windows\winsxs\amd64_microsoft-windows-wpd-portabledevicesqm_31bf3856ad364e35_6.1.7601.17514_none_b11b7e2cfd8c4d39
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\he
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\hr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\hu
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\it
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\id
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\fi
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\fr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\gl
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ga
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\de
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\da
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\el
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\eo
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\es
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\eu
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\et
2,C:\Windows\winsxs\amd64_microsoft-windows-dfsclient-netapi_31bf3856ad364e35_6.1.7600.16385_none_bc912cf74a28a647
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_72\grep\share\locale\sk\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\be
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\bg
2,C:\Windows\winsxs\amd64_microsoft-windows-ie-sysprep_31bf3856ad364e35_8.0.7600.16385_none_924152af4aaf8557
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\ca
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\cs
2,C:\Windows\winsxs\amd64_microsoft-windows-i..er-engine.resources_31bf3856ad364e35_6.1.7601.17514_ja-jp_d4183db432a5f29d
2,C:\Windows\System32\DriverStore\FileRepository\vhdmp.inf_amd64_neutral_c3910bbf4fbccf97
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.SqlClrProvider\10.0.0.0__89845dcd8080cc91
1,C:\Program Files\Tanium\Tanium Server\plugins\console\Dashboards
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\af
2,C:\Windows\winsxs\x86_microsoft-windows-g..licymaker.resources_31bf3856ad364e35_6.1.7600.16385_en-us_59436eb028717570
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_37\grep\share\locale\pt_BR\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\Microsoft.SqlServer#\c988156754e88888de422478835f01a8
2,C:\Windows\System32\DriverStore\FileRepository\faxcn002.inf_amd64_neutral_3d392ccc357e04db
1,C:\Windows\winsxs\x86_wcf-system.runtime.serialization_b03f5f7f11d50a3a_6.1.7601.18532_none_db9f3389dd561754
2,C:\Windows\winsxs\amd64_microsoft.windows.s...smart_card_library_31bf3856ad364e35_6.1.7600.16385_none_55f89e9f01688dc0
2,C:\Windows\winsxs\x86_microsoft-windows-wusa.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6a01eebaaaf68204
1,C:\Windows\winsxs\amd64_microsoft-windows-cryptsvc-dll_31bf3856ad364e35_6.1.7601.22322_none_d4a24ea4ca968363
1,C:\Windows\winsxs\x86_microsoft-windows-ncrypt-dll_31bf3856ad364e35_6.1.7601.18606_none_5ff27b1b4fd45533
2,C:\Windows\winsxs\wow64_microsoft-windows-iis-ftpsvc.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d2857e8176c21a5b
1,C:\Windows\Microsoft.NET\assembly\GAC_32\ISymWrapper\v4.0_4.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\x86_netfx35linq-vb_compiler_orcas_31bf3856ad364e35_6.1.7601.17514_none_9809be824da2c173
2,C:\Windows\winsxs\amd64_microsoft-windows-winrsplugins.resources_31bf3856ad364e35_6.1.7600.16385_en-us_159345c6da1672e1
2,C:\Windows\System32\DriverStore\FileRepository\mdmelsa.inf_amd64_neutral_374f9d31af832d6b
1,C:\Windows\winsxs\wow64_microsoft-windows-kernel32_31bf3856ad364e35_6.1.7601.17965_none_fc038d48a1736e92
2,C:\Windows\System32\DriverStore\FileRepository\mdmdgitn.inf_amd64_neutral_09132735f1063a47
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_98\grep\share\locale\sl\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-workstationservice_31bf3856ad364e35_6.1.7601.17514_none_2a601d5ced714bb5
1,C:\Users\Jim Olsen\AppData\Roaming\Macromedia
2,C:\Windows\winsxs\amd64_microsoft-windows-f..ruetype-iskoolapota_31bf3856ad364e35_6.1.7600.16385_none_2a668cf479ef0388
2,C:\Windows\winsxs\amd64_prnbr005.inf_31bf3856ad364e35_6.1.7600.16385_none_4b6471420f8b03d9\Amd64
2,C:\Windows\winsxs\x86_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_pt-pt_ef7b9e173a536f62
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.WebServiceTask
2,C:\Windows\winsxs\msil_microsoft.windows.smc_31bf3856ad364e35_6.1.7601.17514_none_ab698c2bf8d20bb5
2,C:\Windows\winsxs\amd64_server-help-h1s.dmi_start.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3fb41a083651d00e
2,C:\Windows\winsxs\amd64_microsoft-windows-w..-installer-provider_31bf3856ad364e35_6.1.7601.17514_none_88af1cb8f0d0a95d
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\Microsoft.SqlServer#\a61d501848683192591feaada27f8d6a
2,C:\Windows\winsxs\amd64_netfx-system.directoryservices.protocols_b03f5f7f11d50a3a_6.1.7600.16385_none_f65534c04a41b956
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_34\sqlite
2,C:\Windows\System32\en-US\Licenses\OEM\ServerForSBSolutions
2,C:\Windows\winsxs\amd64_server-help-chm.uim_psync.resources_31bf3856ad364e35_6.1.7600.16385_en-us_1594fbfb8c92ba76
2,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_ru-ru_03775985d5a48f63
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.DirectorySer#\45ec12795950a7d54691591c615a9e3c
2,C:\Windows\SoftwareDistribution\Download
2,C:\Windows\winsxs\amd64_microsoft-windows-dhcpserverrolescript_31bf3856ad364e35_6.1.7600.16385_none_1d6f9bab4827506e
2,C:\Windows\winsxs\amd64_microsoft-windows-t..extension.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a2058f1afade009d
1,C:\Windows\winsxs\msil_system.design_b03f5f7f11d50a3a_6.1.7601.22191_none_72e0ff71d9629a76
2,C:\Windows\winsxs\amd64_microsoft-windows-m..ilerepair.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9ed373c17361cf1b
1,C:\Windows\winsxs\amd64_netfx-aspnet_wp_exe_b03f5f7f11d50a3a_6.1.7601.21884_none_3ad156f04e11776c
2,C:\Windows\winsxs\x86_microsoft-windows-smss.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e4408e86c08891fe
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_71\hash
2,C:\Windows\winsxs\amd64_microsoft-windows-dumpata_31bf3856ad364e35_6.1.7600.16385_none_c5330fa587ba01cb
2,C:\Windows\winsxs\wow64_microsoft-windows-iis-httperrorsbinaries_31bf3856ad364e35_6.1.7600.16385_none_645d1c1b24ec87a4
1,C:\Windows\winsxs\amd64_microsoft-windows-kernelbase_31bf3856ad364e35_6.1.7601.22436_none_859e60b5e45fc488
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_195\grep\share\locale\de\LC_MESSAGES
2,C:\Windows\System32\DriverStore\FileRepository\mdmmotou.inf_amd64_neutral_eb1d978f38f35bca
1,C:\Windows\assembly\GAC_MSIL\PresentationBuildTasks
2,C:\Windows\winsxs\x86_microsoft-windows-o..tend-apis.resources_31bf3856ad364e35_6.1.7601.17514_en-us_a1eb9485bb71c8ff
2,C:\Windows\winsxs\x86_microsoft-windows-d..asks-sync.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ebe6abced058440e
2,C:\Windows\winsxs\amd64_microsoft-windows-acledit.resources_31bf3856ad364e35_6.1.7600.16385_en-us_853b0789da5b1e2a
1,C:\Windows\assembly\GAC_MSIL\PresentationUI
2,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_bg-bg_69bd10c883a3a560
2,C:\Windows\winsxs\amd64_nulhpopr.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9bbc515b6b831d6c
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.S63fb36fa#
2,C:\Windows\winsxs\amd64_microsoft-windows-directx-directinput_31bf3856ad364e35_6.1.7600.16385_none_798d0be3255fc46e
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_73\grep\share\locale\pl\LC_MESSAGES
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Runtime.InteropServices\v4.0_4.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_prnca00x.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_20983167eda7589c
2,C:\Windows\winsxs\x86_microsoft-windows-a..ce-useractionrecord_31bf3856ad364e35_6.1.7600.16385_none_32c4b0bc55387f75
2,C:\Windows\winsxs\x86_microsoft-windows-u..erservice.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f09dccd4f32812c2
2,C:\Windows\winsxs\amd64_microsoft-windows-e..-enforcement-client_31bf3856ad364e35_6.1.7600.16385_none_3efbe964e010a5aa
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.DTSUtilities\v4.0_11.0.0.0__89845dcd8080cc91
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.S0677a649#\1084b6e3c3f1ca2e0c25c6526e62654c
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.ServiceModel.Activation
2,C:\Windows\winsxs\x86_microsoft-windows-a..managerui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_443db5647679d4a2
2,C:\Windows\winsxs\amd64_microsoft-windows-comctl32-v5.resources_31bf3856ad364e35_6.1.7600.16385_es-es_be8a1256afbafd72
2,C:\Windows\SysWOW64\config\systemprofile\AppData\Local\Microsoft\Windows\History
1,C:\Program Files\Tanium\Tanium Server\CertificateBackup2014-11-17-11-17-33
2,C:\Windows\winsxs\x86_microsoft-windows-l..oundation.resources_31bf3856ad364e35_6.1.7601.17514_en-us_ed0314fe47faf776
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Build.Uti#\bdd68f916d6b74807e688e18cab5eb12
2,C:\Windows\winsxs\x86_microsoft-windows-t..p-utility.resources_31bf3856ad364e35_6.1.7601.17514_en-us_f6719a27fd39b2db
2,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-20005_31bf3856ad364e35_6.1.7600.16385_none_ad62bf63006659ce
2,C:\Windows\Boot\EFI
2,C:\Windows\SoftwareDistribution
1,C:\Windows\winsxs\amd64_microsoft-windows-smss_31bf3856ad364e35_6.1.7601.18113_none_0a5f8ec22fd235a9
1,C:\Users\Jim Olsen\AppData\LocalLow\Microsoft\Windows\AppCache
2,C:\Windows\winsxs\x86_microsoft-windows-i..er-engine.resources_31bf3856ad364e35_6.1.7601.17514_en-us_492959f9bd028207
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_194\grep\share\locale\sl\LC_MESSAGES
2,C:\Windows\winsxs\x86_microsoft.grouppoli..t.interop.resources_31bf3856ad364e35_6.1.7601.17514_en-us_864e7d76ac8023f8
1,C:\Windows\winsxs\wow64_microsoft-windows-ieframe_31bf3856ad364e35_11.2.9600.17358_none_515bfcaff7832a25
2,C:\Windows\winsxs\wow64_microsoft-windows-w..lient-aux.resources_31bf3856ad364e35_7.5.7601.17514_en-us_292a8b37a9ef3b8c
2,C:\Windows\winsxs\amd64_microsoft-windows-lmhsvc_31bf3856ad364e35_6.1.7601.17514_none_b0e6edd606f5c524
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.FileSystemTask
2,C:\Windows\System32\DriverStore\FileRepository\netw5v64.inf_amd64_neutral_a6b778ba802632cc
2,C:\Windows\winsxs\amd64_microsoft-windows-fax-service_31bf3856ad364e35_6.1.7601.17514_none_0b499f2c96e8f6b2
2,C:\Windows\winsxs\amd64_policy.1.2.microsof..op.security.azroles_31bf3856ad364e35_6.1.7600.16385_none_48aef4ef4511d002
2,C:\Windows\winsxs\amd64_microsoft-windows-n..entclient.resources_31bf3856ad364e35_6.1.7600.16385_en-us_556b4448d5492f53
2,C:\Windows\winsxs\x86_microsoft-windows-s..iprovider.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d661f15bff622f11
1,C:\Windows\assembly\GAC\Microsoft.VisualStudio.TextManager.Interop.8.0\8.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_microsoft-windows-help-efs.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7b42dfac415afe76
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_111\grep\share\locale\it\LC_MESSAGES
2,C:\Windows\winsxs\amd64_server-help-chm.cluadmin.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c295debf1a270b88
2,C:\Windows\winsxs\msil_microsoft.storage.sancommon.ui_31bf3856ad364e35_6.1.7600.16385_none_ae1ac5ca1447e687
1,C:\Windows\assembly\GAC_MSIL\Microsoft.ReportViewer.WebForms.resources\11.0.0.0_ru_89845dcd8080cc91
2,C:\Windows\winsxs\x86_microsoft-windows-l..nterprise.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2519d7bb63a0a215
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.ServiceModel.Discovery
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-0000046d_31bf3856ad364e35_6.1.7601.22739_none_5c7e78b78577319d
2,C:\Windows\winsxs\amd64_prnle003.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e295a15dbf1fb4e2
1,C:\Windows\winsxs\amd64_microsoft-windows-msauditevtlog_31bf3856ad364e35_6.1.7601.22814_none_25f2098ca82ab2b6
2,C:\Windows\winsxs\amd64_microsoft-windows-directory-services-sam_31bf3856ad364e35_6.1.7601.17514_none_10145eccb79418a5
2,C:\Windows\winsxs\amd64_prnrc004.inf_31bf3856ad364e35_6.1.7600.16385_none_21e7809d8e910def
2,C:\Windows\SysWOW64\en-US\Licenses\eval\ServerWinFoundation
2,C:\Windows\winsxs\amd64_microsoft-windows-t..rvices-rdp-direct3d_31bf3856ad364e35_6.1.7601.17514_none_ce0cf746a97a2699
2,C:\Windows\winsxs\amd64_netfx-microsoft.build.framework_b03f5f7f11d50a3a_6.1.7601.17514_none_4c9eab58e2f91183
2,C:\Windows\assembly\GAC_MSIL\Microsoft.Vsa.Vb.CodeDOMProcessor
2,C:\Windows\winsxs\amd64_microsoft-windows-snmp-evntcmd_31bf3856ad364e35_6.1.7600.16385_none_14f9b9481db6293b
1,C:\Windows\winsxs\amd64_microsoft-windows-crypt32-dll_31bf3856ad364e35_6.1.7601.18205_none_b9a17b06f46a70ad
2,C:\Windows\winsxs\x86_microsoft-windows-services-svchost_31bf3856ad364e35_6.1.7600.16385_none_b591afc466a15356
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_111\grep\share\locale\da\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-crypt32-dll_31bf3856ad364e35_6.1.7601.22736_none_ba0baff00d9f723d
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.V44fb6cc1#\c22a9c70fab67e42ae3261bb7f4f161a
2,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Security.#
1,C:\Users\Jim Olsen\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\BNYMB63B
2,C:\Windows\winsxs\amd64_microsoft-windows-i..nternetcontrolpanel_31bf3856ad364e35_8.0.7601.17514_none_0819f2b6df7a1335
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_71\grep\man
1,C:\Windows\assembly\GAC_64\PresentationCore
1,C:\Windows\winsxs\amd64_microsoft-windows-c..ityclient.resources_31bf3856ad364e35_6.1.7601.22705_en-us_c37ab478cf88f76c
1,C:\Windows\winsxs\amd64_microsoft-windows-t..appserver-licensing_31bf3856ad364e35_6.1.7601.22843_none_05443aa46b33e0f6
2,C:\Windows\winsxs\wow64_microsoft-windows-linkinfo_31bf3856ad364e35_6.1.7600.16385_none_9eaece15f365da54
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\UIAutomationProvider\v4.0_4.0.0.0__31bf3856ad364e35
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_193\grep\share\locale\et\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-help-medexp.resources_31bf3856ad364e35_6.1.7600.16385_en-us_befb9293a1b699ff
2,C:\Windows\winsxs\amd64_wcf-infocardcpl_cpl_31bf3856ad364e35_6.1.7600.16385_none_f578352b168f8a4a
2,C:\Windows\winsxs\wow64_microsoft-windows-rpc-local_31bf3856ad364e35_6.1.7601.17514_none_1c754ed890149b9b
2,C:\Windows\winsxs\x86_microsoft-windows-s..s-svchost.resources_31bf3856ad364e35_6.1.7600.16385_en-us_511f46fd08cd38e1
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_110\grep\share\locale
2,C:\Windows\winsxs\amd64_microsoft-windows-n..formance_monitoring_31bf3856ad364e35_6.1.7600.16385_none_56431363e2cb6652
1,C:\Windows\winsxs\amd64_microsoft-windows-s..-downlevel.binaries_31bf3856ad364e35_6.3.9600.17280_none_5f668c1aff756211
2,C:\Windows\winsxs\wow64_microsoft-windows-b..ions-upload-manager_31bf3856ad364e35_6.1.7600.16385_none_55c5e6b6f1327ce8
2,C:\Windows\winsxs\amd64_microsoft-windows-l..priseia64.resources_31bf3856ad364e35_6.1.7601.17514_en-us_efc948f916800d2c
2,C:\Windows\winsxs\x86_microsoft-windows-m..ss-components-jetes_31bf3856ad364e35_6.1.7600.16385_none_36886cdd2e3bf7e4
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_106\grep\share\locale\nl\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-performancetoolsgui_31bf3856ad364e35_6.1.7601.17514_none_fa2fc39ab7937a51
1,C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE\CommonExtensions\Microsoft\VB\LanguageService\10.0
1,C:\Windows\winsxs\amd64_microsoft-windows-scripting-jscript_31bf3856ad364e35_8.0.7601.17866_none_fb8c2be784ec8fa3
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.Sdc7a71f3#\14662593f5706e2a4e0656c44910b5a7
1,C:\Users\Jim Olsen\Documents\SQL Server Management Studio\Templates\ItemTemplates
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Windows.Controls.Ribbon\v4.0_4.0.0.0__b77a5c561934e089
2,C:\Windows\winsxs\x86_microsoft-windows-m..do-backcompat-tlb20_31bf3856ad364e35_6.1.7601.17514_none_ed1e95de5057e009
2,C:\Windows\winsxs\x86_wcf-m_svc_mod_end_perf_vrg_31bf3856ad364e35_6.1.7600.16385_none_cc6e74aeed7ec870
1,C:\Windows\winsxs\msil_dfsmgmt_31bf3856ad364e35_6.1.7601.21844_none_90f2cf948a12956a
1,C:\Program Files (x86)\Microsoft SQL Server\110\DAC\bin\1033
1,C:\Windows\winsxs\x86_microsoft-windows-e..yphenation.binaries_31bf3856ad364e35_6.3.9600.16428_none_eb9b0f6fb3a13f1e
1,C:\Windows\winsxs\amd64_microsoft-windows-ncrypt-dll_31bf3856ad364e35_6.1.7601.22099_none_bc3c57b22195c1a0
2,C:\Windows\winsxs\amd64_server-help-h1s.tpmadmin.resources_31bf3856ad364e35_6.1.7600.16385_en-us_8224af4d6f3430df
2,C:\Windows\winsxs\amd64_microsoft-windows-t..r-tlntsvr.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ae3d0be2b1c4024c
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_23\grep\share\locale\id\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_48\grep\share\locale\sl\LC_MESSAGES
2,C:\Windows\winsxs\x86_microsoft-windows-diantz_31bf3856ad364e35_6.1.7600.16385_none_a69c6a8f23f521f3
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-behaviors.resources_31bf3856ad364e35_11.2.9600.16428_en-us_09ce26d2c0c6976f
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Xaml.Hosting
2,C:\Windows\winsxs\amd64_microsoft-windows-font-bitmap-fixed_31bf3856ad364e35_6.1.7600.16385_none_db04d3f548508fd9
1,C:\Windows\winsxs\wow64_microsoft-windows-audio-audiocore_31bf3856ad364e35_6.1.7601.18619_none_df1f60782f9ba191
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\PresentationFramework.Aero\v4.0_4.0.0.0__31bf3856ad364e35
1,C:\Windows\winsxs\amd64_microsoft-windows-b..vironment-os-loader_31bf3856ad364e35_6.1.7601.22780_none_b98696ee9ca07f56
2,C:\Windows\System32\DriverStore\FileRepository\netathrx.inf_amd64_neutral_905772087ff288af
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Runt93d54979#
2,C:\Windows\winsxs\x86_microsoft-windows-qedit.resources_31bf3856ad364e35_6.1.7600.16385_en-us_1c748d197640a543
2,C:\Windows\winsxs\amd64_microsoft-windows-p..unterinfrastructure_31bf3856ad364e35_6.1.7600.16385_none_cd7aeeff1897d018
2,C:\Windows\winsxs\amd64_mdmcxpv6.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d07101ecaa44c4af
2,C:\Windows\winsxs\amd64_microsoft-windows-f..type-leelawadeebold_31bf3856ad364e35_6.1.7600.16385_none_4b86f8e6a3279ad0
2,C:\Windows\winsxs\amd64_microsoft-windows-font-truetype-batang_31bf3856ad364e35_6.1.7600.16385_none_13de7dc07ffbe591
2,C:\Windows\winsxs\amd64_microsoft-windows-f..etype-timesnewroman_31bf3856ad364e35_6.1.7601.17514_none_3b958c66aff6cdb7
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\DTSInstall\2f59443741e5c4caa4994e63993688d3
2,C:\Windows\Help\Windows\en-US
2,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-28592_31bf3856ad364e35_6.1.7600.16385_none_b188802cfdb67997
2,C:\Windows\winsxs\amd64_netr28x.inf_31bf3856ad364e35_6.1.7600.16385_none_f6bd180f0177aea7
2,C:\Program Files\Common Files\SpeechEngines\Microsoft
2,C:\Windows\winsxs\x86_microsoft-windows-fmifs_31bf3856ad364e35_6.1.7600.16385_none_56e4c7a892eacb36
2,C:\ProgramData\Microsoft\Windows\Ringtones
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Microsoft.Se29577f5#
2,C:\Windows\winsxs\amd64_microsoft-windows-s..iprovider.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9f12d80e121cae5a
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\Accessibility\0483c93466914f3fbd5b44454b0c8a98
2,C:\Windows\winsxs\x86_microsoft-windows-servicingstack_31bf3856ad364e35_6.1.7600.16385_none_0935b76c289e0fd5
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_193\grep\share\locale\tr\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_6.1.7601.17514_none_678566b7ddea04a5
2,C:\Windows\System32\DriverStore\FileRepository\prnsa002.inf_amd64_neutral_d9df1d04d8cbe336
2,C:\Windows\SoftwareDistribution\SelfUpdate\Handler
2,C:\Windows\winsxs\x86_netfx-mscorwks_dll_b03f5f7f11d50a3a_6.1.7601.17514_none_06b9b03ceb862f7d
1,C:\Windows\ServiceProfiles\LocalService\AppData\Roaming\Microsoft\Network\Connections
1,C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome
1,C:\Windows\winsxs\amd64_microsoft-windows-d..fontcache.resources_31bf3856ad364e35_7.1.7601.16492_cs-cz_dcc5802a4c09b643
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.VisualStudio.Language.CallHierarchy\v4.0_10.0.0.0__b03f5f7f11d50a3a
2,C:\Windows\winsxs\amd64_server-help-chm.uim_snis.resources_31bf3856ad364e35_6.1.7600.16385_en-us_46b28c625df92198
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_198\grep\share\locale\af\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-ntdll_31bf3856ad364e35_6.1.7601.18247_none_b6df585112e2f85b
2,C:\Windows\winsxs\msil_blbmmc_31bf3856ad364e35_6.1.7600.16385_none_1e0d17ddf7df43c4
2,C:\Windows\winsxs\amd64_microsoft-windows-terminalservices-rdpdr_31bf3856ad364e35_6.1.7601.17514_none_5f60151d5fa6ce24
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_122\grep\share\locale\nb\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-storport_31bf3856ad364e35_6.1.7601.18386_none_85588aa4470585ac
2,C:\Windows\winsxs\msil_napsnap_31bf3856ad364e35_6.1.7600.16385_none_0c6dbb690a333628
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\Microsoft.Sfab66633#
2,C:\Windows\assembly\GAC_64\Microsoft.Security.ApplicationId.PolicyManagement.PolicyEngineApi.Interop\6.1.0.0__31bf3856ad364e35
2,C:\Windows\winsxs\amd64_wpf-presentationhostdll_31bf3856ad364e35_6.1.7601.17514_none_ce3172a8369ec608
2,C:\Windows\Microsoft.NET\Framework\v2.0.50727\ASP.NETWebAdminFiles\Security\Users
2,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_sl-si_e951b6c1dfd4bd76
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_63\grep\share\locale\hu\LC_MESSAGES
2,C:\Windows\assembly\NativeImages_v2.0.50727_64\Narrator
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ro
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ru
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\rw
2,C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.ConsoleHost\1.0.0.0__31bf3856ad364e35
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\sr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\sv
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\sk
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\sl
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_122\sqlite
2,C:\Windows\System32\DriverStore\FileRepository\clusdisk.inf_amd64_neutral_517fb8e5b41452c5
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\pl
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\pt
1,C:\Windows\winsxs\x86_microsoft-windows-a..tigations.resources_31bf3856ad364e35_6.1.7601.22248_zh-hk_7a625d3eef48924c
1,C:\Program Files (x86)\Microsoft Visual Studio 10.0\Web\Snippets\HTML\1033
2,C:\Windows\winsxs\amd64_microsoft-windows-s..-vbscript.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6bd0dc3389c765b1
1,C:\Windows\winsxs\amd64_microsoft-windows-t..torclient.resources_31bf3856ad364e35_7.1.7601.16398_en-us_8de2d8fedf1df9ff
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\vi
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\EnvDTE90\d45d934fb4f734451fae61288d59ee9b
2,C:\Windows\winsxs\amd64_microsoft-windows-oleaccrc.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5c4db2c1103b4a92
2,C:\Windows\winsxs\amd64_microsoft-windows-t..es-commandlinetools_31bf3856ad364e35_6.1.7601.17514_none_42d65ed50fa3c682
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\tr
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.ServiceModel.Primitives
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\uk
2,C:\Windows\winsxs\amd64_microsoft-windows-p..ll-events.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3eddeca774028e07
1,C:\Windows\winsxs\x86_caspol_b03f5f7f11d50a3a_6.1.7601.22733_none_29677a47c628119e
2,C:\Windows\winsxs\amd64_tsusbhubfilter.inf_31bf3856ad364e35_6.1.7601.17514_none_776b19f55ac34470
2,C:\Windows\winsxs\amd64_microsoft-windows-g..rveradmintools-gpmc_31bf3856ad364e35_6.1.7601.17514_none_1458f05bc75eb3f4
1,C:\Program Files\Tanium\Tanium Server\ApacheBackup2014-09-16-20-44-23\modules
2,C:\Windows\winsxs\amd64_prnrc006.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_39360e96965fde25
2,C:\Windows\winsxs\amd64_microsoft-windows-a..mecontrol.resources_31bf3856ad364e35_6.1.7600.16385_en-us_392ce9a7ba4fe7e8
2,C:\Windows\winsxs\x86_microsoft-windows-c..us-runtime-stclient_31bf3856ad364e35_6.1.7600.16385_none_a9649d04c661942c
1,C:\Windows\winsxs\wow64_microsoft-windows-ie-htmlapplication_31bf3856ad364e35_8.0.7601.22777_none_dcda8f78e4ab7dd6
2,C:\Windows\winsxs\amd64_microsoft-windows-wmilib_31bf3856ad364e35_6.1.7600.16385_none_b549ebfe1dddb7f1
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\be
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\bg
2,C:\Windows\winsxs\amd64_microsoft-windows-s..packerror.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d2f18e90bddce0c2
2,C:\Windows\winsxs\amd64_microsoft-windows-p..track-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c13d58e431d898bb
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ca
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\cs
2,C:\Windows\winsxs\amd64_prnca00h.inf_31bf3856ad364e35_6.1.7600.16385_none_e0755475742561ac
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_113\grep\share\locale\ca\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-winsrv-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c01e7ca36d3191ee
1,C:\Windows\winsxs\x86_microsoft-windows-m..al-backcompat-tlb28_31bf3856ad364e35_6.1.7601.22012_none_ac6ebffcc80ba2a2
2,C:\Windows\winsxs\amd64_microsoft-windows-c..dtc-runtime-cluster_31bf3856ad364e35_6.1.7601.17514_none_f4ae54a1a351cc34
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\af
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\fr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\fi
2,C:\Windows\winsxs\amd64_microsoft-windows-p..randprintui-asyncui_31bf3856ad364e35_6.1.7600.16385_none_d7d643c30bd72bf4
2,C:\Windows\winsxs\amd64_microsoft-windows-i..tional-codepage-949_31bf3856ad364e35_6.1.7600.16385_none_2ad09128b4ec905d
1,C:\Windows\winsxs\amd64_microsoft-windows-m..do-backcompat-tlb28_31bf3856ad364e35_6.1.7601.17857_none_48be78e20913e405
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\gl
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ga
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\da
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\de
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\eu
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\et
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\es
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\el
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\eo
1,C:\Windows\assembly\NativeImages_v4.0.30319_64\System.Activities
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ja
1,C:\Windows\winsxs\amd64_microsoft-windows-scripting-vbscript_31bf3856ad364e35_11.2.9600.17280_none_2acd701742dec536
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\System.Configuratio#\f02737c83305687a68c088927a6c5a98
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ky
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\ko
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_97\grep\share\locale\ca\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\he
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\hu
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\hr
2,C:\Windows\winsxs\amd64_microsoft-windows-videoport_31bf3856ad364e35_6.1.7600.16385_none_180f3dba1e158073
2,C:\Windows\winsxs\amd64_microsoft-windows-d..andlinepropertytool_31bf3856ad364e35_6.1.7601.17514_none_696354579779eadf
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\id
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\it
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\nb
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\nl
2,C:\Windows\winsxs\amd64_microsoft-windows-n..-domain-clients-svc_31bf3856ad364e35_6.1.7601.17514_none_a2347d4102a4c8ad
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_192\grep\share\locale\lt
1,C:\Windows\winsxs\wow64_microsoft-windows-ie-datacontrol_31bf3856ad364e35_11.2.9600.16428_none_00b2e64ae9989845
1,C:\Windows\assembly\GAC_MSIL\Microsoft.SqlServer.Management.SqlParser\11.0.0.0__89845dcd8080cc91
2,C:\Windows\winsxs\amd64_microsoft-windows-wmi-core-svc_31bf3856ad364e35_6.1.7601.17514_none_fed8c13f0d90a8cf
2,C:\Windows\System32\DriverStore\FileRepository\prnbr004.inf_amd64_neutral_a78e168d6944619a
2,C:\Windows\winsxs\amd64_microsoft-windows-e..rformancemonitoring_31bf3856ad364e35_6.1.7600.16385_none_0d7e44ffcdcf5676
2,C:\Program Files\Common Files\Microsoft Shared\ink\ru-RU
2,C:\Windows\SysWOW64\IME\imekr8\dicts
2,C:\Windows\winsxs\x86_microsoft-windows-s..-binaries.resources_31bf3856ad364e35_6.1.7601.17514_ja-jp_8602279f8341f235
2,C:\Windows\winsxs\x86_microsoft-windows-tapi2xclient.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e8e4d27156d257c9
1,C:\Windows\winsxs\amd64_wpf-presentationhostdll_31bf3856ad364e35_6.1.7601.17755_none_ce07370e36be4971
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_186\grep\share\locale\ru\LC_MESSAGES
1,C:\Windows\winsxs\msil_system.messaging_b03f5f7f11d50a3a_6.1.7601.18523_none_020fbc17e044566c
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_108\grep\share\locale\pt_BR\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\napsnap\f64692e58aa1a7116024bf3c3cbd1352
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_53\grep\share\locale\sr\LC_MESSAGES
1,C:\Users\MSSQL$SQLEXPRESS\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch
2,C:\Windows\winsxs\amd64_microsoft-windows-tabletpc-uihub_31bf3856ad364e35_6.1.7600.16385_none_6f7e04cab5e74750
1,C:\Program Files\Microsoft SQL Server\110\DTS\ForEachEnumerators\en
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_194\grep\share\locale\vi\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-msf.resources_31bf3856ad364e35_6.1.7601.17514_en-us_810c155fd815ebfc
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\Microsoft.GroupPoli#\fb058c5e3b9d3af4bfa69811b3a498c1
2,C:\Windows\SysWOW64\en-US\Licenses\_Default\ServerMediumBusinessSecurity
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_105\grep\share\locale\nb\LC_MESSAGES
2,C:\Windows\winsxs\wow64_microsoft-windows-mfmjpegdec_31bf3856ad364e35_6.1.7600.16385_none_7fa793baa201214e
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_198\grep\share\locale\ru\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft-windows-i..riptedsandboxplugin_31bf3856ad364e35_11.2.9600.17420_none_3e33a8dd806ae83c
2,C:\Windows\winsxs\x86_microsoft-windows-m..ac-sql-cliconfg-rll_31bf3856ad364e35_6.1.7600.16385_none_6a546f37bbab5475
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_21\grep\share\locale\lt\LC_MESSAGES
2,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\zh_TW
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_64\grep\share\locale\pt_BR\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-s..y-spp-wmi.resources_31bf3856ad364e35_6.1.7600.16385_en-us_4185c7bb7887e34e
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_98\grep\share\locale\hr\LC_MESSAGES
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_34\hash
1,C:\Windows\winsxs\amd64_microsoft-windows-d..s-ime-japanese-core_31bf3856ad364e35_6.1.7601.18556_none_cd680cfea4662663
2,C:\Windows\winsxs\amd64_microsoft-windows-p..rtmonitor.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a317442b915afa21
1,C:\Program Files (x86)\Common Files\microsoft shared\MSEnv\1033
1,C:\Windows\assembly\NativeImages_v4.0.30319_32\Presentatio84a6349c#\63e9d81bd805aea8f8690fee2efc9a9e
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_191\grep\share\locale\da\LC_MESSAGES
2,C:\Windows\winsxs\x86_microsoft-windows-m..do-backcompat-tlb25_31bf3856ad364e35_6.1.7601.17514_none_ece8864250806bbe
2,C:\Windows\winsxs\amd64_microsoft-windows-help-adm_31bf3856ad364e35_6.1.7600.16385_none_893d90cda53294d1
2,C:\Windows\assembly\NativeImages_v2.0.50727_32\StorageMgmt
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-memoryanalyzer_31bf3856ad364e35_11.2.9600.17420_none_a54ee356089ed8d3
1,C:\Windows\winsxs\amd64_microsoft-windows-gc-usbforcereboot_31bf3856ad364e35_6.1.7601.18328_none_92f16c0a70dcfacc
2,C:\Windows\winsxs\x86_microsoft-windows-f..temcompareutilities_31bf3856ad364e35_6.1.7600.16385_none_009cfaa696afe78b
1,C:\Windows\winsxs\amd64_microsoft.vc80.mfc_1fc8b3b9a1e18e3b_8.0.50727.1833_none_8442d417329336b1
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-antiphishfilter_31bf3856ad364e35_11.2.9600.17420_none_dde9e18b80cbedfe
2,C:\Windows\winsxs\amd64_prnkm004.inf_31bf3856ad364e35_6.1.7600.16385_none_50ff82015b97b704
2,C:\Windows\winsxs\wow64_microsoft-windows-msxml60_31bf3856ad364e35_6.1.7601.17514_none_f0e8ac03e1d6bb5b
2,C:\Windows\winsxs\amd64_prnep00b.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6cfd9c5115587d13
1,C:\Windows\Migration\WTR
2,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_ro-ro_010f0df9d729cc93
1,C:\Windows\winsxs\amd64_microsoft-windows-installer-engine_31bf3856ad364e35_6.1.7601.18604_none_61ab3ea4ca1c4419
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_195\grep\share\locale\he\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-u..assdriver.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e5eb83baa658d423
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.SqlServer.FTPTaskUI
1,C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.IdentityModel.Services\v4.0_4.0.0.0__b77a5c561934e089
2,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_18\grep\contrib\grep\2.5.4\grep-2.5.4-src
2,C:\Users\All Users\Microsoft\Windows\Sqm\Sessions
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_116\grep\share\locale\de\LC_MESSAGES
2,C:\Windows\winsxs\x86_microsoft-windows-p..topeercollab-client_31bf3856ad364e35_6.1.7600.16385_none_9d0ba9d0ec2082dd
2,C:\Windows\winsxs\x86_microsoft-windows-nddeapi.resources_31bf3856ad364e35_6.1.7600.16385_en-us_de6a8036f7c9134b
2,C:\Windows\System32\ko-KR
1,C:\Windows\winsxs\x86_microsoft-windows-authentication-authui_31bf3856ad364e35_6.1.7601.18276_none_0dbbeb9453d8f782
2,C:\Windows\winsxs\x86_netfx-mscorsn_dll_b03f5f7f11d50a3a_6.1.7600.16385_none_6adff9151d65c2d5
1,C:\Windows\winsxs\amd64_microsoft-windows-e..yphenation.binaries_31bf3856ad364e35_6.3.9600.16428_none_47b9aaf36bfeb054
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_98\yara
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_47\grep\share\locale\hu\LC_MESSAGES
2,C:\Windows\winsxs\amd64_microsoft-windows-help-netwl.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6d1db8e7c7a5a558
2,C:\Windows\winsxs\amd64_microsoft-windows-i..eyboard-korean_101c_31bf3856ad364e35_6.1.7600.16385_none_e1bb6033344e9a8a
2,C:\Windows\winsxs\amd64_microsoft-windows-t..languages.resources_31bf3856ad364e35_6.1.7601.17514_it-it_9dadd996d9880aa1
2,C:\Windows\winsxs\x86_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_sl-si_d44bd64014e9029b
2,C:\Windows\winsxs\wow64_microsoft-windows-powershell-sip_31bf3856ad364e35_6.1.7600.16385_none_ceb83cd750c49126
1,C:\Windows\winsxs\x86_netfx35linq-framework_assemblylist_31bf3856ad364e35_6.1.7600.16385_none_d2345696aab11309
1,C:\Windows\assembly\GAC_MSIL\Microsoft.VisualBasic
1,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\vi\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.DirectorySer#\c1cdea55f62c9e8b9b9c1ae4c23b1c1f
1,C:\Windows\winsxs\amd64_wcf-m_tx_bridge_perf_c_vrg_31bf3856ad364e35_6.1.7600.16385_none_de4eced846c25e95
1,C:\Windows\winsxs\x86_microsoft-windows-iscsi_initiator_ui_31bf3856ad364e35_6.1.7600.16385_none_d7c180d4bd657495
1,C:\Windows\winsxs\wow64_microsoft-windows-p..st-common.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d0db429429b01e85
1,C:\Windows\assembly\GAC_32\Microsoft.Interop.Security.AzRoles\2.0.0.0__31bf3856ad364e35
1,C:\Windows\assembly\GAC_32\Microsoft.Security.ApplicationId.PolicyManagement.PolicyEngineApi.Interop\6.1.0.0__31bf3856ad364e35
1,C:\Windows\System32\DriverStore\FileRepository\ehstorcertdrv.inf_amd64_neutral_2e1cecffae9c899a
1,C:\Windows\winsxs\msil_microsoft.windows.s..downlevel.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a0646737018f58e9
1,C:\Windows\winsxs\amd64_microsoft-windows-i..tional-codepage-855_31bf3856ad364e35_6.1.7600.16385_none_2adcbc7eb4e3273f
1,C:\Windows\Resources\Themes\aero\en-US
1,C:\Windows\winsxs\amd64_microsoft-windows-f..client-applications_31bf3856ad364e35_6.1.7601.17514_none_d71fb1d63f05ef22
1,C:\Windows\winsxs\amd64_ql2300.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5504a7062024cd6a
1,C:\Windows\Boot\PCAT\tr-TR
1,C:\Windows\winsxs\x86_microsoft-windows-rasapi.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5ca843a91ebaba76
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Windows.Forms\6c352ff9e3603b0e69d969ff7e7632f5
1,C:\Windows\winsxs\x86_netfx-dw_b03f5f7f11d50a3a_6.1.7600.16385_none_a223bd3dd785391a
1,C:\Windows\winsxs\amd64_microsoft-windows-ntshrui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_544475ff2d69ee9f
1,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_ar-sa_6d63d528d41932e2
1,C:\Windows\winsxs\msil_microsoft.web.manag..davclient.resources_31bf3856ad364e35_6.1.7600.16385_en-us_acee5ff0a4855329
1,C:\Windows\winsxs\x86_microsoft-windows-l..anagement.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6c43d2b67bf26136
1,C:\Windows\winsxs\x86_microsoft-windows-m..drivermanager-trace_31bf3856ad364e35_6.1.7601.17514_none_817af6649fbc1ed4
1,C:\Windows\System32\DriverStore\FileRepository\mdmtexas.inf_amd64_neutral_7572473d88d69307
1,C:\Windows\winsxs\amd64_netb57va.inf_31bf3856ad364e35_6.1.7600.16385_none_581eb8ede4375d14
1,C:\Windows\winsxs\amd64_microsoft-windows-wmi-provider-common_31bf3856ad364e35_6.1.7600.16385_none_0434b662f2d183a0
1,C:\Windows\winsxs\x86_microsoft-windows-b..oad-isapi.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5a4b9d403c1122c9
1,C:\Windows\winsxs\amd64_usbprint.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_754e23e2d81789cd
1,C:\Windows\winsxs\amd64_microsoft-windows-powercpl_31bf3856ad364e35_6.1.7601.17514_none_c006f86a8ad7ce0f
1,C:\Windows\winsxs\amd64_microsoft-windows-i..henticationbinaries_31bf3856ad364e35_6.1.7600.16385_none_39dd2292c22c1d9e
1,C:\Windows\winsxs\amd64_microsoft-windows-p..ng-server-isolation_31bf3856ad364e35_6.1.7600.16385_none_f8a40495785334a9
1,C:\Windows\winsxs\x86_microsoft-windows-upnpssdp.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9fada492807dfef9
1,C:\Windows\winsxs\x86_microsoft-windows-photoscreensaver_31bf3856ad364e35_6.1.7601.17514_none_6dd5e8c3b6b81894
1,C:\Windows\winsxs\amd64_prnbr007.inf_31bf3856ad364e35_6.1.7600.16385_none_4c7695ac41c77cab\Amd64
1,C:\Windows\Boot\PCAT\sv-SE
1,C:\Windows\winsxs\amd64_ds-ui-ext.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7a2b039113f0c5bf
1,C:\Windows\SysWOW64\NetworkList\Icons\StockIcons
1,C:\Windows\winsxs\amd64_microsoft-windows-com-dtc-runtime-tm_31bf3856ad364e35_6.1.7601.17514_none_f7be9391315f6cc3
1,C:\Windows\winsxs\x86_microsoft-windows-r..-commandline-editor_31bf3856ad364e35_6.1.7600.16385_none_316a8a208c030e56
1,C:\Windows\winsxs\amd64_microsoft-windows-webdavredir-mrxdav_31bf3856ad364e35_6.1.7601.17514_none_72d0eaa6dc5b2edb
1,C:\Windows\winsxs\amd64_tsportalweb_31bf3856ad364e35_6.1.7600.16385_none_9dbdffcbeee4e7d9
1,C:\Windows\winsxs\amd64_display.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_8bb90e0956a02ab0
1,C:\Windows\winsxs\amd64_wiasa002.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_499baeb321ffb611
1,C:\Windows\winsxs\amd64_microsoft-windows-whea-troubleshooter_31bf3856ad364e35_6.1.7600.16385_none_124dff546524b2a8
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Management.A#\009a09f5b2322bb8c5520dc5ddbb28bb
1,C:\Windows\winsxs\amd64_prnrc00c.inf_31bf3856ad364e35_6.1.7600.16385_none_3b11d85d2b1e2536\Amd64
1,C:\Windows\winsxs\x86_microsoft-windows-i..emsupport.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ffbf5574b0e45521
1,C:\Windows\winsxs\wow64_microsoft-windows-i..sideincludebinaries_31bf3856ad364e35_6.1.7601.17514_none_64b6ec2d7d52abe9
1,C:\Windows\SysWOW64\config\systemprofile\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\1FA4OC0L
1,C:\Windows\winsxs\amd64_microsoft-windows-c..rvices-ca.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ab9cb2499d423544
1,C:\Windows\SysWOW64\Msdtc
1,C:\Windows\winsxs\amd64_microsoft-windows-s..r-library.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6336f71e6582b89f
1,C:\Windows\winsxs\x86_microsoft-windows-a..oldertool.resources_31bf3856ad364e35_6.1.7600.16385_en-us_1326ac88fbb14d64
1,C:\Windows\winsxs\amd64_microsoft-windows-m..ctory-rll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_352074d8f36e57ca
1,C:\Windows\winsxs\amd64_prnep00c.inf_31bf3856ad364e35_6.1.7600.16385_none_adb67b12e1bb863e\Amd64
1,C:\Windows\winsxs\x86_microsoft-windows-t..omruntime.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d4aac73d55c29ea7
1,C:\Windows\winsxs\amd64_microsoft-windows-c..plus-admin-comadmin_31bf3856ad364e35_6.1.7600.16385_none_8d5620dbd8b24529
1,C:\Windows\winsxs\x86_microsoft-windows-wpd-shellextension_31bf3856ad364e35_6.1.7601.17514_none_13305696250bcb70
1,C:\Windows\winsxs\amd64_microsoft-windows-sens-client_31bf3856ad364e35_6.1.7600.16385_none_5d37a06dd6d242cc
1,C:\Windows\winsxs\amd64_microsoft-windows-n..ols-local.resources_31bf3856ad364e35_6.1.7600.16385_en-us_0f50fd0b5ec629aa
1,C:\Windows\winsxs\amd64_microsoft-windows-shell32_31bf3856ad364e35_6.1.7601.17514_none_ca4f304d289b7800
1,C:\Windows\winsxs\x86_microsoft-windows-wimgapi.resources_31bf3856ad364e35_6.1.7600.16385_en-us_192dea2a21d5c43a
1,C:\Windows\winsxs\msil_system.web.mobile_b03f5f7f11d50a3a_6.1.7601.17514_none_ac4cc83a8cbcb7cf
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_26\hash
1,C:\Windows\winsxs\amd64_netfx-aspnet_filter_dll_b03f5f7f11d50a3a_6.1.7600.16385_none_622a42c0ffb29a66
1,C:\Windows\System32\en-US\Licenses\_Default\ServerForSBSolutions
1,C:\Windows\System32\en-US\Licenses\OEM\ServerFoundation
1,C:\Windows\winsxs\amd64_microsoft-windows-tpm-adm_31bf3856ad364e35_6.1.7600.16385_none_47f0687a93cc8b71
1,C:\Windows\winsxs\x86_netfx-system_tlb_b03f5f7f11d50a3a_6.1.7600.16385_none_a7142cd751e0387d
1,C:\Windows\winsxs\x86_microsoft-windows-c..ilter-rtf.resources_31bf3856ad364e35_7.0.7600.16385_en-us_876ea0bdb3b0741b
1,C:\Windows\winsxs\amd64_microsoft-windows-r..workerdisplaydriver_31bf3856ad364e35_6.1.7601.17514_none_fac082804ac20fda
1,C:\Windows\winsxs\x86_microsoft-windows-c..ervices-certocm-dll_31bf3856ad364e35_6.1.7600.16385_none_09fbe46869ff9deb
1,C:\Windows\winsxs\amd64_microsoft-windows-m..oledb-rll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d36dbea01368547a
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.Transactions\051655963f24f9ade08486084c570086
1,C:\Windows\winsxs\amd64_prnkm005.inf_31bf3856ad364e35_6.1.7600.16385_none_5188943674b5f36d\Amd64
1,C:\Windows\winsxs\amd64_microsoft-windows-oobe-machine-ui_31bf3856ad364e35_6.1.7601.17514_none_c081339cf850430b
1,C:\Windows\winsxs\amd64_microsoft-windows-unimodem-core_31bf3856ad364e35_6.1.7600.16385_none_f08d2472ee3ef611
1,C:\Windows\winsxs\amd64_microsoft-windows-defrag-core.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d011c12457bd2a09
1,C:\Windows\System32\DriverStore\FileRepository\hal.inf_amd64_neutral_232b95977cf6d84c
1,C:\Windows\winsxs\amd64_wiabr006.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d74bc45bcdcee83f
1,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-28596_31bf3856ad364e35_6.1.7600.16385_none_b15d407cfdd6e95b
1,C:\Windows\winsxs\x86_microsoft-windows-b..-bcdtemplate-server_31bf3856ad364e35_6.1.7600.16385_none_02d116158e776d78
1,C:\Windows\winsxs\amd64_microsoft-windows-i..rvice-gui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f4775dec15c35e5e
1,C:\Windows\winsxs\wow64_microsoft-windows-c..complus-eventsystem_31bf3856ad364e35_6.1.7600.16385_none_73373b169fcf68cb
1,C:\Windows\winsxs\x86_microsoft-windows-d..r-commandline-setup_31bf3856ad364e35_6.1.7601.17514_none_cdcc88d9c65a0433
1,C:\Windows\winsxs\x86_microsoft-windows-class_ss_31bf3856ad364e35_6.1.7600.16385_none_17723c290c0f2178
1,C:\Windows\winsxs\amd64_security-malware-windows-defender-events_31bf3856ad364e35_6.1.7600.16385_none_118cf1dcd54a3dea
1,C:\Windows\winsxs\amd64_microsoft-windows-t..nition-server.en-au_31bf3856ad364e35_6.1.7600.16385_none_c26220fd6869c57b
1,C:\Users\Default\AppData\Roaming\Microsoft\Windows\Templates
1,C:\Windows\Help\Help
1,C:\Windows\winsxs\amd64_server-help-h1s.cmak_ops.resources_31bf3856ad364e35_6.1.7600.16385_en-us_cce9012b03ac52a0
1,C:\Windows\winsxs\x86_microsoft-windows-netsh.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2b99b5d32e84c3c0
1,C:\Windows\winsxs\amd64_microsoft-windows-imm32_31bf3856ad364e35_6.1.7600.16385_none_b84b0fbd941c03a9
1,C:\Windows\winsxs\amd64_microsoft-windows-setupcl.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f643d2f900a8eb18
1,C:\Windows\winsxs\amd64_microsoft-windows-s..mhardware.resources_31bf3856ad364e35_6.1.7600.16385_en-us_46b0ac990f93475a
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\napcrypt\d95f343677c556b67e99818cc02f4214
1,C:\Windows\winsxs\x86_microsoft-windows-unimodem-config_31bf3856ad364e35_6.1.7600.16385_none_f4d7f7b17ffe522a
1,C:\Windows\winsxs\amd64_microsoft-windows-netbios-netapi_31bf3856ad364e35_6.1.7600.16385_none_3453fc4c6aafb4c5
1,C:\Windows\winsxs\amd64_microsoft-windows-a..ience-common-logger_31bf3856ad364e35_6.1.7600.16385_none_c9643ae2e72c5455
1,C:\Windows\winsxs\amd64_microsoft-windows-qos-adm_31bf3856ad364e35_6.1.7600.16385_none_2fd86548de3136ed
1,C:\Windows\winsxs\amd64_microsoft-windows-help-appman.resources_31bf3856ad364e35_6.1.7600.16385_en-us_49a224ccd23196d9
1,C:\Windows\winsxs\amd64_server-help-h1s.recovery_start.resources_31bf3856ad364e35_6.1.7600.16385_en-us_61645e1e815a5581
1,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-00010480_31bf3856ad364e35_6.1.7601.17514_none_f268daa7a212eb80
1,C:\Windows\winsxs\amd64_microsoft-windows-i..personalization-adm_31bf3856ad364e35_6.1.7600.16385_none_b641570ee85bac92
1,C:\Windows\winsxs\amd64_microsoft-windows-servicereportingapi_31bf3856ad364e35_6.1.7600.16385_none_c895144f92ce0a2e
1,C:\Users\Jim Olsen\AppData\Local\Microsoft\Feeds Cache\VSDSKGLM
1,C:\Windows\winsxs\x86_microsoft-windows-netplwiz-exe.resources_31bf3856ad364e35_6.1.7600.16385_en-us_fdf0e52976537440
1,C:\Windows\winsxs\x86_microsoft-windows-i..ional-codepage-1143_31bf3856ad364e35_6.1.7600.16385_none_2262c2c76b576a26
1,C:\Windows\winsxs\amd64_microsoft-windows-ldap-client.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3760db0440b81fb3
1,C:\Windows\winsxs\msil_microsoft.applicationid.rulewizard_31bf3856ad364e35_6.1.7601.17514_none_d26690f13d498f9d
1,C:\Windows\winsxs\x86_microsoft-windows-n..erclasses.resources_31bf3856ad364e35_6.1.7600.16385_en-us_74ff7604b8c68a3c
1,C:\Windows\System32\sysprep\en-US
1,C:\Windows\System32\slmgr
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_19\grep\share\locale\pt_BR\LC_MESSAGES
1,C:\Windows\System32\DriverStore\FileRepository\prnlx00v.inf_amd64_neutral_86ff307c66080d00\Amd64
1,C:\Windows\winsxs\amd64_microsoft-windows-tapiservice_31bf3856ad364e35_6.1.7601.17514_none_4162de4afb9222c0
1,C:\Windows\winsxs\x86_microsoft-windows-d..ices-boot-files-x86_31bf3856ad364e35_6.1.7601.17514_none_be30acd81c856db7
1,C:\Windows\winsxs\amd64_microsoft-windows-f..acefilter.resources_31bf3856ad364e35_6.1.7600.16385_en-us_141cb78b27158555
1,C:\Windows\winsxs\amd64_microsoft-windows-d..pwindowmanager-core_31bf3856ad364e35_6.1.7601.17514_none_ebc99983d3d18578
1,C:\Users\Public\Videos\Sample Videos
1,C:\Windows\winsxs\x86_microsoft-windows-http-api_31bf3856ad364e35_6.1.7601.17514_none_f7b3a6eafb8df2de
1,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-20838_31bf3856ad364e35_6.1.7600.16385_none_ae962ee8ffa4883e
1,C:\Windows\winsxs\x86_microsoft-windows-acluifilefoldertool_31bf3856ad364e35_6.1.7600.16385_none_ed99f3aa1077f7e1
1,C:\Windows\winsxs\amd64_msmouse.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2d64a68aafc8bd0f
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-0000044e_31bf3856ad364e35_6.1.7601.17514_none_5c7743f26c0495bb
1,C:\Windows\winsxs\amd64_server-help-h1s.ipsecpolicy.resources_31bf3856ad364e35_6.1.7600.16385_en-us_be7580dd24e9ffdf
1,C:\Windows\winsxs\x86_microsoft-windows-t..ty-client.resources_31bf3856ad364e35_6.1.7600.16385_en-us_402c144309f85a9b
1,C:\Windows\winsxs\amd64_microsoft-windows-mlang.resources_31bf3856ad364e35_6.1.7600.16385_sk-sk_ca73b0dc729ea456
1,C:\Windows\winsxs\wow64_microsoft-windows-scripting_31bf3856ad364e35_6.1.7600.16385_none_aeb1ef0f4e6bba1d
1,C:\Windows\winsxs\amd64_microsoft-windows-t..lipboardredirection_31bf3856ad364e35_6.1.7601.17514_none_5ffc161221c1b4f6
1,C:\Windows\winsxs\msil_system.data.services.design_b77a5c561934e089_6.1.7601.17514_none_1d40772755ce4438
1,C:\Windows\winsxs\amd64_wialx005.inf_31bf3856ad364e35_6.1.7600.16385_none_063f1c91b3be1d84
1,C:\Windows\security\msscw\bin
1,C:\Windows\winsxs\amd64_microsoft-windows-r..-commandline-editor_31bf3856ad364e35_6.1.7600.16385_none_8d8925a444607f8c
1,C:\Windows\winsxs\amd64_microsoft-windows-s..ilenotify.resources_31bf3856ad364e35_7.0.7600.16385_en-us_90e2906d41481f23
1,C:\Windows\winsxs\amd64_microsoft-windows-s..erbox-isv.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d6e7b259751e89a9
1,C:\Boot\es-ES
1,C:\Windows\winsxs\amd64_microsoft-windows-help-printp.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7ce5f517410188b5
1,C:\Windows\winsxs\amd64_microsoft-windows-font-bitmap-courier_31bf3856ad364e35_6.1.7600.16385_none_5283fef09ca6fa1a
1,C:\Windows\security\msscw\Policies
1,C:\Windows\System32\DriverStore\FileRepository\prnca00f.inf_amd64_neutral_777b6911d18869b7\Amd64
1,C:\Windows\System32\spool
1,C:\Windows\winsxs\amd64_microsoft-windows-directshow-vfw-capture_31bf3856ad364e35_6.1.7601.17514_none_34a42c333d8f8d28
1,C:\Windows\winsxs\x86_microsoft-windows-themeui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9dca7b0ecf029c4b
1,C:\Windows\winsxs\amd64_microsoft-windows-t..ices-appcompattools_31bf3856ad364e35_6.1.7600.16385_none_4f148138856f7090
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\Microsoft.Security.#\3710621dc3c65616c4f62bd92619fe01
1,C:\Windows\winsxs\amd64_avc.inf_31bf3856ad364e35_6.1.7600.16385_none_084e3f0eabcf1e24
1,C:\Windows\winsxs\x86_wcf-m_svc_mod_end_perf_reg_31bf3856ad364e35_6.1.7600.16385_none_c6aaf278f1332711
1,C:\Windows\winsxs\amd64_netfx-aspnet_webadmin_locres_res_b03f5f7f11d50a3a_6.1.7600.16385_none_6db55c2fd0300a34
1,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\hu\LC_MESSAGES
1,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_nb-no_7522e7f20c7b85ee
1,C:\Windows\PLA\Templates
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00020422_31bf3856ad364e35_6.1.7600.16385_none_89e4f7a262c2326c
1,C:\Windows\winsxs\x86_naphlpr_31bf3856ad364e35_6.1.7601.17514_none_0d1b28e7082c222d
1,C:\Windows\winsxs\amd64_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_hu-hu_330f86d55de64a40
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00040402_31bf3856ad364e35_6.1.7600.16385_none_d021ad4447e4399c
1,C:\Windows\winsxs\amd64_microsoft-windows-b..nager-efi.resources_31bf3856ad364e35_6.1.7600.16385_cs-cz_97769b281ba398b8
1,C:\Windows\winsxs\x86_policy.1.7.microsoft.ink_31bf3856ad364e35_6.1.7600.16385_none_465aa985a7bc61de
1,C:\Windows\winsxs\amd64_microsoft-windows-g..lorer-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a98f8df3953bd666
1,C:\Windows\winsxs\amd64_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_pl-pl_48647f8af4b7dcd8
1,C:\Windows\winsxs\msil_microsoft.iis.power...provider.resources_31bf3856ad364e35_6.1.7601.17514_en-us_eee506200bd43e29
1,C:\Windows\winsxs\amd64_acpipmi.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ac73b2c5fc356f15
1,C:\Windows\winsxs\amd64_microsoft-windows-a..leshooter.resources_31bf3856ad364e35_6.1.7600.16385_en-us_669ed37c9f94ce9e
1,C:\Windows\assembly\GAC_MSIL\System.Windows.Forms
1,C:\Windows\winsxs\amd64_microsoft-windows-t..direction.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d31879ba5162faa3
1,C:\Windows\winsxs\x86_microsoft-windows-cryptdll-dll_31bf3856ad364e35_6.1.7600.16385_none_0574dc0a0f190696
1,C:\Windows\winsxs\amd64_netfx35linq-csharp_31bf3856ad364e35_6.1.7601.17514_none_7551b4792ac9630d
1,C:\Windows\assembly\GAC_MSIL\SetupNfsIdMap\1.0.0.0__31bf3856ad364e35
1,C:\Windows\winsxs\x86_microsoft-windows-directx-direct3dxof_31bf3856ad364e35_6.1.7600.16385_none_af4b5c30460b0358
1,C:\Windows\winsxs\amd64_microsoft-windows-sstext3d.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e5626780fc684f08
1,C:\Windows\assembly\GAC_MSIL\Microsoft.Build.Framework
1,C:\Windows\winsxs\amd64_microsoft-windows-e..host-peer.resources_31bf3856ad364e35_6.1.7600.16385_en-us_861592c73a32a46d
1,C:\Windows\winsxs\amd64_mdmmcom.inf_31bf3856ad364e35_6.1.7600.16385_none_812d4a3d3edaed64
1,C:\Windows\Microsoft.NET\Framework\v2.0.50727\CONFIG
1,C:\Windows\assembly\GAC_32\mscorlib\2.0.0.0__b77a5c561934e089
1,C:\Windows\SysWOW64\en-US\Licenses\_Default\ServerHPC
1,C:\Users\Default\AppData\Local\Microsoft\Windows\History
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Storage.N#\d4c3336a2a5e78ca273d6c2d22b4141f
1,C:\Windows\winsxs\amd64_microsoft-windows-classpnp_31bf3856ad364e35_6.1.7601.17514_none_73a9340ac2b15f83
1,C:\Windows\winsxs\amd64_microsoft-windows-isoburn.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2ce31c084eed585c
1,C:\Windows\winsxs\x86_microsoft-windows-i..ional-codepage-1361_31bf3856ad364e35_6.1.7600.16385_none_2181876f6be7c708
1,C:\Windows\winsxs\amd64_microsoft-windows-mp4sdecd_31bf3856ad364e35_6.1.7600.16385_none_6add5a3b86da385d
1,C:\Windows\winsxs\x86_microsoft-windows-display.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9b4ebaf32f78312e
1,C:\Windows\winsxs\amd64_dot4.inf_31bf3856ad364e35_6.1.7600.16385_none_3868f74cf5b51f17
1,C:\Windows\winsxs\x86_netfx-tlbref_dll_b03f5f7f11d50a3a_6.1.7600.16385_none_3598d90610375bf9
1,C:\Windows\winsxs\amd64_microsoft-hyper-v-vstack-vmwp.resources_31bf3856ad364e35_6.1.7601.17514_en-us_ded3834ec7a40179
1,C:\Windows\winsxs\x86_microsoft-windows-wlanui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_26d1644143d9fd30
1,C:\Windows\winsxs\amd64_microsoft-windows-kernelstreaming_31bf3856ad364e35_6.1.7601.17514_none_b5a6c7c6ac83a58e
1,C:\Windows\winsxs\msil_microsoft.web.management.remoting_31bf3856ad364e35_6.1.7600.16385_none_9ae2cfe7153c9c91
1,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-00001009_31bf3856ad364e35_6.1.7600.16385_none_510928a0b00d5cf9
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_23\grep\share\locale\bg\LC_MESSAGES
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.JScript
1,C:\Windows\winsxs\x86_microsoft-windows-wlan-extension_31bf3856ad364e35_6.1.7600.16385_none_f9b9855184ad1e6d
1,C:\Windows\winsxs\amd64_microsoft-windows-fsrm-cli_31bf3856ad364e35_6.1.7601.17514_none_994a68062a39e26a
1,C:\Windows\winsxs\x86_microsoft-windows-s..mhardware.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ea9211155735d624
1,C:\Windows\Microsoft.NET\Framework\v1.1.4322
1,C:\Windows\winsxs\x86_microsoft-windows-mydocs_31bf3856ad364e35_6.1.7601.17514_none_41fecee29ca47686
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\Microsoft.Build.Fra#
1,C:\Windows\winsxs\amd64_brmfcumd.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ce61ed8f7bb6c5c2
1,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-00020408_31bf3856ad364e35_6.1.7600.16385_none_96e2fa98956cdc4f
1,C:\Windows\winsxs\amd64_microsoft-windows-i..tional-codepage-850_31bf3856ad364e35_6.1.7600.16385_none_2add2e66b4e2a71a
1,C:\Program Files\Common Files\Microsoft Shared\ink\fsdefinitions\keypad
1,C:\Windows\winsxs\amd64_microsoft-windows-c..mplus-admin-comrepl_31bf3856ad364e35_6.1.7600.16385_none_45fe6fe8a9201e55
1,C:\Windows\winsxs\x86_microsoft-windows-n..tconfigui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_4227739b2aca8a41
1,C:\Windows\winsxs\amd64_microsoft-windows-sysdm_31bf3856ad364e35_6.1.7601.17514_none_c0a8382e8bdc6241
1,C:\Windows\winsxs\amd64_microsoft-windows-i..itiator_service_mof_31bf3856ad364e35_6.1.7601.17514_none_0793641fcc6ca405
1,C:\Windows\winsxs\x86_microsoft-windows-w..rastructure-upgrade_31bf3856ad364e35_6.1.7600.16385_none_54780cc7e444c076
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-0001045d_31bf3856ad364e35_6.1.7600.16385_none_fcf2d63d61f04474
1,C:\Windows\winsxs\amd64_microsoft-windows-cdosys.resources_31bf3856ad364e35_6.1.7601.17514_ru-ru_0791e80f29948eec
1,C:\Windows\winsxs\amd64_microsoft-windows-l..nterprise.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3399f79d1f2be99f
1,C:\Windows\winsxs\amd64_microsoft-windows-a..ence-mitigations-c4_31bf3856ad364e35_6.1.7600.16385_none_681a2aaf0bfabe79
1,C:\Windows\winsxs\amd64_microsoft-windows-r..-agilevpn.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7b400e7afb13d576
1,C:\Windows\winsxs\amd64_microsoft-windows-s..on-native.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3d213b1c5ad75b99
1,C:\Windows\winsxs\x86_microsoft-windows-wmi-scripting_31bf3856ad364e35_6.1.7600.16385_none_60e78eba5410cd9e
1,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-20273_31bf3856ad364e35_6.1.7600.16385_none_b092e3ecfe5774df
1,C:\Windows\winsxs\amd64_microsoft-windows-i..rendering.resources_31bf3856ad364e35_8.0.7600.16385_en-us_8397a46594202519
1,C:\Windows\winsxs\amd64_microsoft-windows-blb-srv-main_31bf3856ad364e35_6.1.7601.17514_none_71c3d70622d35cd1
1,C:\Windows\winsxs\amd64_microsoft-windows-tcpip-nettcpip-pro_31bf3856ad364e35_6.1.7600.16385_none_0451aba3e9d81445
1,C:\Windows\winsxs\amd64_server-help-h1s.ie_esc_start.resources_31bf3856ad364e35_6.1.7600.16385_en-us_dcc5a009b8e6f070
1,C:\Windows\winsxs\amd64_1394.inf_31bf3856ad364e35_6.1.7601.17514_none_59555c0e1c877c53
1,C:\Windows\winsxs\amd64_microsoft-windows-r..-licensing-external_31bf3856ad364e35_6.1.7600.16385_none_7fb3a862109d27c1
1,C:\Windows\assembly\GAC_MSIL\StorageMgmt\1.0.0.0__31bf3856ad364e35
1,C:\Windows\winsxs\amd64_microsoft-windows-previousversions-adm_31bf3856ad364e35_6.1.7600.16385_none_41d785d4f443b620
1,C:\Windows\SysWOW64\en-US\Licenses\_Default\ServerStorageWorkgroup
1,C:\Windows\winsxs\msil_srmcontentcls_31bf3856ad364e35_6.1.7601.17514_none_e184fd73e068da9c
1,C:\Windows\winsxs\amd64_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_es-es_48e7908e86b464c2
1,C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\NonCritical_x64_2069f6a335b3a4a48372e5aa5a4778d07e65bb_cab_0415737a
1,C:\Windows\winsxs\x86_microsoft-windows-f..mutilityntfslibrary_31bf3856ad364e35_6.1.7601.17514_none_00cb21b8522f43ec
1,C:\Windows\winsxs\amd64_microsoft-windows-i..ablenetworkgraphics_31bf3856ad364e35_8.0.7600.16385_none_6475a807a41c7313
1,C:\Windows\winsxs\amd64_microsoft-windows-r..-web-administration_31bf3856ad364e35_6.1.7600.16385_none_14ad17a973a02eef
1,C:\Windows\System32\DriverStore\FileRepository\prnca00c.inf_amd64_neutral_510c36849918ce92\Amd64
1,C:\Windows\winsxs\x86_microsoft-windows-content-filter-mime_31bf3856ad364e35_7.0.7601.17514_none_4a78bd97fed17642
1,C:\Windows\winsxs\amd64_microsoft-windows-i..nese-domainlexicons_31bf3856ad364e35_6.1.7600.16385_none_4475ba47a78dc96f
1,C:\Windows\winsxs\amd64_server-help-chm.hra.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c9340e34b643b974
1,C:\Windows\winsxs\msil_microsoft.wsman.management.resources_31bf3856ad364e35_6.1.7601.17514_en-us_2cc0337200422e57
1,C:\Windows\winsxs\x86_microsoft-windows-l..standardv.resources_31bf3856ad364e35_6.1.7600.16385_en-us_24740be6f8aec455
1,C:\Windows\assembly\GAC_MSIL\Microsoft.BackgroundIntelligentTransfer.Management
1,C:\Windows\winsxs\wow64_microsoft.windows.d..eshootingpackmodule_31bf3856ad364e35_6.1.7600.16385_none_876e3b6d44107d5a
1,C:\Windows\winsxs\msil_microsoft.web.management_31bf3856ad364e35_6.1.7601.17514_none_c74e13bcdb41d354
1,C:\Windows\ServiceProfiles\NetworkService\AppData\Roaming\Microsoft\Windows\Printer Shortcuts
1,C:\Windows\winsxs\amd64_wcf-wsatconfig_b03f5f7f11d50a3a_6.1.7601.17514_none_d7ce65f32404434b
1,C:\Windows\winsxs\x86_microsoft-windows-compact.resources_31bf3856ad364e35_6.1.7600.16385_en-us_cd993ca7dc92d5bd
1,C:\Windows\winsxs\amd64_microsoft-windows-i..-service-mmc-snapin_31bf3856ad364e35_6.1.7600.16385_none_76a3e7136851eccf
1,C:\Windows\winsxs\amd64_microsoft-windows-i..mentation.resources_31bf3856ad364e35_8.0.7600.16385_en-us_8effe3e3ea5c3179
1,C:\Windows\winsxs\x86_microsoft-windows-tzutil.resources_31bf3856ad364e35_6.1.7600.16385_en-us_778b563beafa23fc
1,C:\Windows\winsxs\x86_microsoft-windows-c..tionauthorityclient_31bf3856ad364e35_6.1.7601.17514_none_d9851f679ae9a131
1,C:\Windows\winsxs\amd64_microsoft-windows-rasbase-rassstp_31bf3856ad364e35_6.1.7601.17514_none_f7f7b561fe8c0735
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\SrpUxSnapIn\780e5b2898b2cd49f5823dffac3b5e93
1,C:\Windows\winsxs\x86_microsoft-windows-wlanutil_31bf3856ad364e35_6.1.7600.16385_none_3aee095e6f5dd427
1,C:\Windows\winsxs\amd64_server-help-h1s.connmgr.resources_31bf3856ad364e35_6.1.7600.16385_en-us_5888e4ac7bb21565
1,C:\Windows\winsxs\x86_microsoft-windows-d..x-directxdiagnostic_31bf3856ad364e35_6.1.7601.17514_none_25cb021dbc0611db
1,C:\Windows\winsxs\x86_microsoft-windows-t..es-umcres.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f81f6ef7ac31ded0
1,C:\Windows\winsxs\x86_microsoft-windows-l..bspremium.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9da2c0857e18bd71
1,C:\Windows\winsxs\amd64_microsoft.windows.h..ocessor-driverclass_31bf3856ad364e35_6.1.7600.16385_none_559906a314d4f487
1,C:\Windows\System32\DriverStore\FileRepository\fdc.inf_amd64_neutral_bbcfca39fdc02275
1,C:\Windows\winsxs\amd64_server-help-h1s.gp_start.resources_31bf3856ad364e35_6.1.7600.16385_en-us_770ec7d28635f3e9
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00000843_31bf3856ad364e35_6.1.7600.16385_none_441dca567d53951f
1,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_pt-pt_12eda1d8afcd225e
1,C:\Windows\winsxs\x86_microsoft-windows-a..wdm-audio.resources_31bf3856ad364e35_6.1.7600.16385_en-us_708a2f68632e24fb
1,C:\Windows\winsxs\x86_microsoft-windows-s..mib-extension-agent_31bf3856ad364e35_6.1.7600.16385_none_7851d1737c2306e6
1,C:\Windows\winsxs\amd64_microsoft-windows-wmvdecod_31bf3856ad364e35_6.1.7601.17514_none_20b089c0f6efacae
1,C:\Windows\winsxs\x86_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_pt-pt_5a9ad8afc4494b64
1,C:\Windows\winsxs\amd64_microsoft-windows-n..ktopology.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c0f2de22c6673991
1,C:\Windows\winsxs\amd64_server-help-chm.sua_lh.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3b1d6c3fb6700623
1,C:\Windows\winsxs\amd64_microsoft-windows-d..-standarddictionary_31bf3856ad364e35_6.1.7600.16385_none_dc7a0a24f48c1886
1,C:\Windows\winsxs\amd64_microsoft-windows-d..yservices-core-perf_31bf3856ad364e35_6.1.7601.17514_none_ad4cf05eee36bd80
1,C:\Windows\winsxs\amd64_microsoft-windows-lsa-msprivs_31bf3856ad364e35_6.1.7600.16385_none_680de2b99516e12e
1,C:\Windows\System32\DriverStore\FileRepository\mdmsii64.inf_amd64_neutral_d7409fccc5ef4078
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Security.#\53628485c538b7d0bde021e842825dc9
1,C:\Windows\winsxs\amd64_microsoft-windows-mmres_31bf3856ad364e35_6.1.7600.16385_none_bacb7329f882f019
1,C:\Windows\winsxs\x86_microsoft-windows-directx-directinput_31bf3856ad364e35_6.1.7600.16385_none_1d6e705f6d025338
1,C:\Windows\winsxs\amd64_microsoft-windows-font-fms.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6b49e6a1a9cb1167
1,C:\Windows\winsxs\wow64_microsoft-windows-netbt_31bf3856ad364e35_6.1.7601.17514_none_c8df7823424473a1
1,C:\Windows\winsxs\x86_microsoft-windows-m..ponents-mdac-sqlwid_31bf3856ad364e35_6.1.7600.16385_none_19511877cece3e8e
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_18\grep\share\locale\it\LC_MESSAGES
1,C:\Windows\System32\IME\IMESC5
1,C:\Windows\winsxs\amd64_fdphost_31bf3856ad364e35_6.1.7600.16385_none_d78d3591881d5b04
1,C:\Windows\winsxs\amd64_microsoft-windows-duser.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d1256a4a3c8105f9
1,C:\Windows\winsxs\amd64_microsoft-windows-g..in-appmgr.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3d8073cfce1a514d
1,C:\Windows\winsxs\amd64_microsoft-windows-comctl32-v5.resources_31bf3856ad364e35_6.1.7600.16385_zh-hk_1cf0186e9791586f
1,C:\Windows\winsxs\amd64_netevbda.inf_31bf3856ad364e35_6.1.7600.16385_none_960cfc4d7aab525d
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Build.Fra#\a71fda14114136e528b310f41dce7915
1,C:\Windows\winsxs\x86_microsoft-windows-d..mc-domainsandtrusts_31bf3856ad364e35_6.1.7601.17514_none_d7c96a868e5d83fb
1,C:\Windows\winsxs\amd64_microsoft-windows-tabletpc-ipsplugin_31bf3856ad364e35_6.1.7600.16385_none_183763f35905b40c
1,C:\Windows\winsxs\amd64_prnky006.inf_31bf3856ad364e35_6.1.7600.16385_none_3ee7affd389bdbca
1,C:\Windows\winsxs\x86_microsoft.windows.s..ation.badcomponents_31bf3856ad364e35_6.1.7600.16385_none_3868158f24725705
1,C:\Windows\winsxs\amd64_microsoft-windows-c..andprompt.resources_31bf3856ad364e35_6.1.7601.17514_en-us_dda7e3a7a889bd4d
1,C:\Windows\winsxs\amd64_microsoft-windows-usermodensi_31bf3856ad364e35_6.1.7600.16385_none_ce571486e124e749
1,C:\Windows\winsxs\amd64_microsoft-windows-u..erservice.resources_31bf3856ad364e35_6.1.7600.16385_en-us_4cbc6858ab8583f8
1,C:\Windows\winsxs\x86_netfx-ado_net_diag_b03f5f7f11d50a3a_6.1.7600.16385_none_41e26933a436d37d
1,C:\Windows\winsxs\amd64_microsoft-windows-audio-mci_31bf3856ad364e35_6.1.7600.16385_none_79024acd05e90673
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Applicati#
1,C:\Windows\winsxs\amd64_microsoft-windows-d..providers.resources_31bf3856ad364e35_6.1.7601.17514_en-us_cf28c79b7f2b526b
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00000465_31bf3856ad364e35_6.1.7600.16385_none_44fca9fa7cc56c13
1,C:\Windows\winsxs\wow64_microsoft-windows-i..humb-shift_keyboard_31bf3856ad364e35_6.1.7600.16385_none_540b0759de0f8281
1,C:\Windows\winsxs\amd64_microsoft-windows-basesrv_31bf3856ad364e35_6.1.7600.16385_none_68bfdc7cfd6bd477
1,C:\Windows\winsxs\wow64_microsoft-windows-i..-wow64-setupdll0011_31bf3856ad364e35_6.1.7600.16385_none_4a9f5a28c99a3ce4
1,C:\Windows\winsxs\amd64_microsoft-windows-timewarpui.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ad300f7dd1b0909d
1,C:\Windows\inf\StarterGPOs\{9C03F88D-8608-44B7-A3E7-7316D1CAC152}\en-US
1,C:\Windows\winsxs\x86_microsoft-windows-installer-handler_31bf3856ad364e35_6.1.7601.17514_none_e0e1f307aa11a690
1,C:\Windows\winsxs\amd64_microsoft-windows-deskmon.resources_31bf3856ad364e35_6.1.7600.16385_en-us_719d68be15dfaf69
1,C:\Windows\winsxs\x86_microsoft-windows-wrp-integrity-client_31bf3856ad364e35_6.1.7600.16385_none_2b1523604c99c736
1,C:\Windows\assembly\GAC_MSIL\Microsoft.ApplicationId.Framework.Resources
1,C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\1KKTRWWM
1,C:\Windows\winsxs\amd64_microsoft-windows-webdavredir-webclient_31bf3856ad364e35_6.1.7601.17514_none_b34bcf2bca512dc2
1,C:\Users\Default\Start Menu
1,C:\Windows\winsxs\amd64_microsoft-windows-d..e-handwritingapplet_31bf3856ad364e35_6.1.7600.16385_none_6a9dcfe209eaa05a
1,C:\Windows\assembly\GAC_MSIL\System.Web.Mobile\2.0.0.0__b03f5f7f11d50a3a
1,C:\Windows\winsxs\amd64_microsoft.remotefil..fsrhelper.resources_31bf3856ad364e35_6.1.7600.16385_en-us_381f55ecea6a2638
1,C:\Windows\winsxs\x86_netfx35linq-msbuild_data_files_31bf3856ad364e35_6.1.7600.16385_none_8cf1b3aadc9746b7
1,C:\Windows\winsxs\x86_microsoft-windows-homegroup-controlpanel_31bf3856ad364e35_6.1.7601.17514_none_b83c28f41f93f405
1,C:\Windows\inf\MSDTC\0000
1,C:\Windows\inf\StarterGPOs\{8780588E-EF91-442B-BD5F-2D50DE7ABF76}\User\en-US
1,C:\Windows\winsxs\amd64_microsoft-windows-aero_ss.resources_31bf3856ad364e35_6.1.7600.16385_en-us_99c539cdc67b85ca
1,C:\Windows\winsxs\amd64_net1yx64.inf_31bf3856ad364e35_6.1.7600.16385_none_4784ec4e3e29c3ed
1,C:\Windows\winsxs\amd64_elxstor.inf_31bf3856ad364e35_6.1.7600.16385_none_08826a22cb03ca5f
1,C:\Windows\winsxs\amd64_aspnet_compiler_b03f5f7f11d50a3a_6.1.7600.16385_none_a5a135380060b978
1,C:\Windows\winsxs\amd64_networking-mpssvc-admin_31bf3856ad364e35_6.1.7601.17514_none_03783362986e804b
1,C:\Windows\winsxs\msil_microsoft.security...anagement.xmlhelper_31bf3856ad364e35_6.1.7600.16385_none_5169d9267766b3da
1,C:\Windows\winsxs\x86_netfx-aspnet_webadmin_secur_res_b03f5f7f11d50a3a_6.1.7600.16385_none_98004846fc315966
1,C:\Users\Public\Downloads
1,C:\Windows\System32\DriverStore\FileRepository\iscsi.inf_amd64_neutral_2ef24e9270d8b2a9
1,C:\Windows\winsxs\amd64_microsoft-windows-servicepackerror_31bf3856ad364e35_6.1.7600.16385_none_eaa0728ab4570513
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_19\grep
1,C:\Windows\winsxs\amd64_prnlx00d.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ea9b85ffa46a0f4e
1,C:\Windows\winsxs\amd64_adpu320.inf_31bf3856ad364e35_6.1.7600.16385_none_f4a210f475e000bb
1,C:\Windows\System32\hu-HU
1,C:\Windows\winsxs\amd64_microsoft-windows-d..show-core.resources_31bf3856ad364e35_6.1.7600.16385_en-us_aaedd68e5784d2c2
1,C:\Windows\winsxs\amd64_mdmmoto1.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_6dcf9ac5d1cdd4b2
1,C:\Windows\ServiceProfiles\NetworkService\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Accessibility
1,C:\Windows\System32\Tasks\Microsoft\Windows
1,C:\Windows\winsxs\amd64_microsoft-windows-t..minalservicesclient_31bf3856ad364e35_6.1.7601.17514_none_ac02530437b71a3f
1,C:\Windows\winsxs\amd64_microsoft-windows-tapiadmin_31bf3856ad364e35_6.1.7601.17514_none_bbdb0b78ef489574
1,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-20002_31bf3856ad364e35_6.1.7600.16385_none_ad832f27004e05fb
1,C:\Windows\winsxs\x86_microsoft-windows-l..priseia64.resources_31bf3856ad364e35_6.1.7601.17514_en-us_93aaad755e229bf6
1,C:\Windows\winsxs\amd64_microsoft-windows-security-spp-ux_31bf3856ad364e35_6.1.7601.17514_none_b9e7a42ab571bbb9
1,C:\Windows\winsxs\amd64_microsoft-windows-tabletpc-controlpanel_31bf3856ad364e35_6.1.7601.17514_none_3d9977977190cdc4
1,C:\Windows\winsxs\amd64_mdmnttp.inf_31bf3856ad364e35_6.1.7600.16385_none_f3bd67b475e3e5c6
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_21\grep\man\cat1
1,C:\Windows\winsxs\amd64_microsoft-windows-d..ain-files.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2fb33b1685175e88
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\System.EnterpriseSe#
1,C:\Windows\SysWOW64\WindowsPowerShell\v1.0\Modules\TroubleshootingPack
1,C:\Windows\winsxs\amd64_microsoft-windows-powershell-exe_31bf3856ad364e35_6.1.7600.16385_none_c50af05b1be3aa2b
1,C:\Windows\winsxs\x86_microsoft-windows-sharedfoldersui_31bf3856ad364e35_6.1.7600.16385_none_b7f38afb92de484f
1,C:\Program Files (x86)\Tanium\Tanium Client\Downloads\Action_18\grep\share\locale\cs\LC_MESSAGES
1,C:\Windows\winsxs\x86_microsoft-windows-s..ionengine.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e91e821e7be12dcf
1,C:\Windows\winsxs\x86_microsoft-windows-wlanpref.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f4a2440848c3d8bf
1,C:\Windows\assembly\GAC_MSIL\napsnap.resources
1,C:\Windows\assembly\GAC_MSIL\Microsoft.BackgroundIntelligentTransfer.Management\1.0.0.0__31bf3856ad364e35
1,C:\Windows\winsxs\amd64_microsoft-windows-com-dtc-runtime_31bf3856ad364e35_6.1.7600.16385_none_7547f48c79b40229
1,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_6.0.7600.16385_hr-hr_f92ec94d1bc52a9e
1,C:\Windows\winsxs\amd64_microsoft-windows-s..csengine-nativehost_31bf3856ad364e35_6.1.7600.16385_none_761ad65676427bd9
1,C:\Windows\System32\en-US\Licenses\_Default\ServerSBSPremium
1,C:\Windows\winsxs\amd64_microsoft.activedirectory.management_31bf3856ad364e35_6.1.7601.17514_none_76bc584f8cc2e2c6
1,C:\Windows\winsxs\amd64_microsoft-windows-sqlliteqp_31bf3856ad364e35_6.1.7600.16385_none_150ca4ff7cfab552
1,C:\Windows\System32\DriverStore\FileRepository\mdmtkr.inf_amd64_neutral_8e3809aa77440c37
1,C:\Windows\winsxs\amd64_microsoft-windows-peertopeerpnrpautoreg_31bf3856ad364e35_6.1.7600.16385_none_3ed59563383363e7
1,C:\Windows\winsxs\amd64_microsoft-windows-errorreportingui_31bf3856ad364e35_6.1.7600.16385_none_2a5a1c441bc85473
1,C:\Windows\winsxs\amd64_mdmags64.inf_31bf3856ad364e35_6.1.7600.16385_none_8abdabbbcd196853
1,C:\Windows\winsxs\amd64_prnlx00z.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_bc5d0503346f1d54
1,C:\Windows\System32\en-US\Licenses\OEM\ServerMediumBusinessMessaging
1,C:\Windows\assembly\GAC_64\naphlpr\6.1.0.0__31bf3856ad364e35
1,C:\Windows\winsxs\x86_microsoft-windows-s..y-secedit.resources_31bf3856ad364e35_6.1.7600.16385_en-us_28d1e537177fb784
1,C:\Windows\assembly\GAC_32\Microsoft.CertificateServices.Setup.Interop
1,C:\Windows\winsxs\amd64_microsoft-windows-nfs-admincore_31bf3856ad364e35_6.1.7601.17514_none_1037adb3f7ba34bd
1,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-0000042c_31bf3856ad364e35_6.1.7600.16385_none_63b7f9b0a40897cc
1,C:\Windows\winsxs\msil_system.addin.contract_b03f5f7f11d50a3a_6.1.7601.17514_none_46152da9482ca76c
1,C:\Windows\winsxs\wow64_microsoft-windows-i..-wow64-setupdll0021_31bf3856ad364e35_6.1.7600.16385_none_4b10e156c951416b
1,C:\Windows\winsxs\amd64_microsoft-windows-a..orecodecs.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a0117050dc6b1274
1,C:\Windows\winsxs\amd64_microsoft-windows-d..twlogging.resources_31bf3856ad364e35_6.1.7600.16385_en-us_f8ee09bcda832671
1,C:\Windows\winsxs\amd64_microsoft-windows-p..ng-server-enablerpc_31bf3856ad364e35_6.1.7600.16385_none_f2db22c8ef251e05
1,C:\Windows\System32\en-US\Licenses\_Default\ServerStorageWorkgroup
1,C:\Windows\winsxs\x86_microsoft-windows-cdosys.resources_31bf3856ad364e35_6.1.7601.17514_fi-fi_01389668157305de
1,C:\Windows\winsxs\x86_netfx-aspnet_roles_sql_b03f5f7f11d50a3a_6.1.7600.16385_none_072d3c4f13092ac3
1,C:\Windows\winsxs\amd64_mdm5674a.inf_31bf3856ad364e35_6.1.7600.16385_none_42fd2975a010a30b
1,C:\Windows\System32\en-US\Licenses\OEM\ServerStorageWorkgroup
1,C:\Windows\winsxs\amd64_microsoft-windows-s..ini-systemtoolsuser_31bf3856ad364e35_6.1.7600.16385_none_7ca09f65fd387e58
1,C:\Windows\ServiceProfiles\NetworkService\AppData\Roaming\Microsoft\SoftwareProtectionPlatform
1,C:\Windows\winsxs\x86_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_tr-tr_7b26e497051a09da
1,C:\Windows\winsxs\wow64_microsoft-windows-i..l-keyboard-0003041e_31bf3856ad364e35_6.1.7600.16385_none_4df5eaef7b29dee4
1,C:\Windows\winsxs\amd64_microsoft-windows-s..ion-agent.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ad23c88fc1f1fa60
1,C:\Windows\winsxs\wow64_microsoft-windows-i..-wow64-setupdll0816_31bf3856ad364e35_6.1.7600.16385_none_4a68944cc9c395a1
1,C:\Windows\winsxs\amd64_microsoft-windows-batmeter.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ce20edd28b74a968
1,C:\Windows\winsxs\x86_microsoft-windows-usbceip.resources_31bf3856ad364e35_6.1.7600.16385_en-us_9bbd54de7ba953bb
1,C:\Windows\assembly\GAC_64\Interop.DfsrHelper
1,C:\Windows\winsxs\amd64_microsoft-windows-xwizards-win32plugin_31bf3856ad364e35_6.1.7600.16385_none_95b0b6e23be86a4a
1,C:\Windows\winsxs\amd64_microsoft-windows-font-fms.resources_31bf3856ad364e35_6.1.7600.16385_bg-bg_23a3473d225f0e38
1,C:\Windows\winsxs\amd64_microsoft-windows-t..s-collaboration-api_31bf3856ad364e35_6.1.7601.17514_none_a39735a9b3e58f7a
1,C:\Windows\winsxs\x86_microsoft-windows-r..onmanager.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2df33a926479c43d
1,C:\Windows\System32\DriverStore\FileRepository\prnms001.inf_amd64_neutral_9b214cd9b78760aa
1,C:\Windows\inf\.NET CLR Data
1,C:\Windows\winsxs\amd64_microsoft-windows-n..sprotection-shvhost_31bf3856ad364e35_6.1.7601.17514_none_3de56b450d5c7940
1,C:\Windows\Boot\EFI\es-ES
1,C:\Windows\winsxs\amd64_microsoft-windows-i..l-keyboard-00000449_31bf3856ad364e35_6.1.7601.17514_none_48f4080a788fce87
1,C:\Windows\winsxs\amd64_microsoft-windows-lsa.resources_31bf3856ad364e35_6.1.7601.17514_en-us_e4cdd9c0ad3ae168
1,C:\Windows\System32\NetworkList
1,C:\Windows\winsxs\amd64_microsoft-windows-nfs-clientshellext_31bf3856ad364e35_6.1.7601.17514_none_b470e2aee6d71603
1,C:\Windows\winsxs\amd64_netl260a.inf.resources_31bf3856ad364e35_6.1.7600.16385_en-us_37d5568c6cab39ba
1,C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.Commands.Management.Resources\1.0.0.0_en_31bf3856ad364e35
1,C:\Windows\winsxs\x86_microsoft-windows-ddoiproxy_31bf3856ad364e35_6.1.7600.16385_none_3f3f4dd85f6845b7
1,C:\Windows\winsxs\amd64_microsoft-windows-t..t-package.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7772712c7303407b
1,C:\Users\Jim Olsen\AppData\Local\Microsoft\Windows\WER\ERC
1,C:\Windows\winsxs\amd64_microsoft-windows-fontext.resources_31bf3856ad364e35_6.1.7600.16385_en-us_15578a9b75ad6a08
1,C:\Windows\winsxs\x86_microsoft-windows-clip_31bf3856ad364e35_6.1.7600.16385_none_a7b238407d550501
1,C:\Windows\winsxs\x86_microsoft-windows-comdlg32.resources_31bf3856ad364e35_6.1.7601.17514_ru-ru_361eafdb1f34fd8e
1,C:\Windows\winsxs\amd64_microsoft-windows-t..es-transportdrivers_31bf3856ad364e35_6.1.7600.16385_none_37a129135e68497e
1,C:\Windows\winsxs\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_zh-cn_19dcac3f6bc16dce
1,C:\Windows\winsxs\amd64_microsoft-windows-tsproxy-edgeadapter_31bf3856ad364e35_6.1.7601.17514_none_9c3078d8e354d9d3
1,C:\Windows\winsxs\amd64_microsoft-windows-printing-adm_31bf3856ad364e35_6.1.7600.16385_none_61aaaebb9aec513d
1,C:\Users\Jim Olsen\Favorites
1,C:\Windows\winsxs\amd64_microsoft-windows-storexpl.resources_31bf3856ad364e35_6.1.7600.16385_en-us_a6a70cad94e7b7c5
1,C:\Windows\winsxs\amd64_microsoft-windows-soundrec-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_c66b3d818988d0f8
1,C:\Windows\winsxs\amd64_microsoft-windows-mssign32-dll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_19ec38460d920c99
1,C:\Windows\assembly\NativeImages_v2.0.50727_64\Microsoft.Storage.N#\d022b32980a544e574e7da3f67d8fefd
1,C:\Windows\winsxs\wow64_microsoft-windows-msf_31bf3856ad364e35_6.1.7600.16385_none_0ecccaeba96f30d2
1,C:\Windows\winsxs\amd64_microsoft-windows-rasserver.resources_31bf3856ad364e35_6.1.7600.16385_en-us_d73605ecd5ec6277
1,C:\Windows\winsxs\amd64_microsoft-windows-b..isc-tools.resources_31bf3856ad364e35_6.1.7600.16385_en-us_3f3bc9163ae8cff9
1,C:\Windows\winsxs\amd64_microsoft-windows-w..ationservice-netapi_31bf3856ad364e35_6.1.7601.17514_none_d3a15c29cbd0ca1d
1,C:\Windows\winsxs\x86_microsoft-windows-shunimpl_31bf3856ad364e35_6.1.7601.17514_none_579de0269297b04b
1,C:\Windows\winsxs\wow64_microsoft-windows-i..ttpredirectbinaries_31bf3856ad364e35_6.1.7600.16385_none_13c790eccc23afcd
1,C:\Windows\winsxs\amd64_microsoft-windows-sethc.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b387b5738168647f
1,C:\Windows\winsxs\amd64_server-help-h1s.dssite.resources_31bf3856ad364e35_6.1.7600.16385_en-us_7065e12fed3edfc5
1,C:\Windows\winsxs\amd64_microsoft-windows-appid.resources_31bf3856ad364e35_6.1.7600.16385_en-us_921f7aaac68bcb70
1,C:\Windows\winsxs\amd64_microsoft-windows-shfolder_31bf3856ad364e35_6.1.7600.16385_none_4b125fb438c5a314
1,C:\Windows\winsxs\amd64_microsoft-windows-p..rnetprinting-client_31bf3856ad364e35_6.1.7601.17514_none_e8f86b1cdf02c483
1,C:\Windows\winsxs\x86_microsoft-windows-comctl32-v5.resources_31bf3856ad364e35_6.1.7600.16385_de-de_b9af43f608588ed2
1,C:\Windows\winsxs\amd64_microsoft-windows-comdlg32_31bf3856ad364e35_6.1.7601.17514_none_13d71710bc471de6
1,C:\Windows\winsxs\amd64_microsoft-windows-rasrtutils_31bf3856ad364e35_6.1.7601.17514_none_6b3b9980011a19de
1,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-10010_31bf3856ad364e35_6.1.7600.16385_none_809f8138e204f251
1,C:\Windows\System32\DriverStore\FileRepository\prnrc005.inf_amd64_neutral_31e08a1c2f933124
1,C:\Windows\winsxs\amd64_ricoh.inf_31bf3856ad364e35_6.1.7600.16385_none_74eae2fb3c9f26c1
1,C:\Windows\winsxs\amd64_microsoft-hyper-v-vstack-vmwp_31bf3856ad364e35_6.1.7601.17514_none_936693b5766832b2
1,C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft
1,C:\Windows\winsxs\x86_microsoft-windows-t..cesframework-msimtf_31bf3856ad364e35_6.1.7600.16385_none_d15bda804befe6a3
1,C:\Windows\System32\Microsoft\Protect\S-1-5-18
1,C:\Windows\System32\DriverStore\FileRepository\mdmzyxlg.inf_amd64_neutral_14f9249844f1cf17
1,C:\Windows\winsxs\FileMaps
1,C:\Windows\System32\DriverStore\FileRepository\netevbda.inf_amd64_neutral_bab421df9c31cc81
1,C:\Windows\winsxs\amd64_microsoft-windows-i..onal-codepage-20932_31bf3856ad364e35_6.1.7600.16385_none_aed6f7a8ff73fa39
1,C:\Windows\System32\DriverStore\FileRepository\rdpbus.inf_amd64_neutral_3b741ca76444b9c3
1,C:\Windows\SysWOW64\en-US\Licenses\OEM\ServerEssentialManagement
1,C:\Windows\winsxs\amd64_microsoft-windows-tapisetup_31bf3856ad364e35_6.1.7600.16385_none_c5e81c6ab4db0c88
1,C:\Windows\winsxs\amd64_microsoft-windows-wlanpref.resources_31bf3856ad364e35_6.1.7600.16385_en-us_50c0df8c012149f5
1,C:\Windows\winsxs\x86_microsoft-windows-crypt32-dll.resources_31bf3856ad364e35_6.1.7600.16385_en-us_cdfd33b21b9a0a10
1,C:\Windows\winsxs\amd64_microsoft-windows-pshed.resources_31bf3856ad364e35_6.1.7600.16385_en-us_ef89364392d56738
1,C:\Program Files (x86)\Tanium\Tanium Client\Tools\StdUtils\grep\share\locale\tr\LC_MESSAGES
1,C:\Windows\winsxs\amd64_wpdcomp.inf_31bf3856ad364e35_6.1.7601.17514_none_d7b74761221e6838
1,C:\Windows\winsxs\x86_microsoft-windows-icacls_31bf3856ad364e35_6.1.7600.16385_none_328af534074dc6cc
1,C:\Windows\winsxs\amd64_microsoft-windows-p..ooler-networkclient_31bf3856ad364e35_6.1.7601.17514_none_9799402887898e33
1,C:\Windows\winsxs\amd64_microsoft-windows-help-peopcom.resources_31bf3856ad364e35_6.1.7600.16385_en-us_633a37f23953d5bf
1,C:\Windows\winsxs\amd64_microsoft-windows-adfs-federationservice_31bf3856ad364e35_6.1.7600.16385_none_4a0ceb894c22f4d6
1,C:\Windows\Resources\Themes\aero\Shell\NormalColor
1,C:\Windows\System32\DriverStore\FileRepository\prnca00i.inf_amd64_neutral_09ff5ee0a0cf0233
1,C:\Windows\winsxs\x86_microsoft-windows-m..ents-mdac-ado15-vbs_31bf3856ad364e35_6.1.7600.16385_none_1475db23cc8131bc
1,C:\Windows\assembly\GAC_MSIL\System.Web.Services
1,C:\Windows\winsxs\amd64_netfx35linq-system...a.datasetextensions_31bf3856ad364e35_6.1.7601.17514_none_b547268892a0926f
1,C:\Windows\winsxs\amd64_microsoft-windows-mediaplayer-wmvcore_31bf3856ad364e35_6.1.7601.17514_none_6558893cec770b80
1,C:\Windows\winsxs\amd64_microsoft-windows-s..enter-adm.resources_31bf3856ad364e35_6.1.7600.16385_en-us_dae5b4c8881a63c6
1,C:\Windows\winsxs\amd64_microsoft-windows-ime-korean-padresource_31bf3856ad364e35_6.1.7600.16385_none_9ec00f34a33a1929
1,C:\Windows\assembly\GAC_MSIL\TaskScheduler.Resources
1,C:\Windows\winsxs\x86_microsoft-windows-wmi-stdprov-provider_31bf3856ad364e35_6.1.7600.16385_none_3e64b54427e2eb11
1,C:\Windows\winsxs\amd64_microsoft-windows-ie-vgx_31bf3856ad364e35_8.0.7600.16385_none_63e64a49796df6a6
1,C:\Windows\winsxs\amd64_microsoft-windows-grouppolicy-gptext_31bf3856ad364e35_6.1.7600.16385_none_9344be31a8b7d6bd
1,C:\Windows\winsxs\amd64_microsoft-windows-c..er-server.resources_31bf3856ad364e35_6.1.7600.16385_en-us_e45aebf7ceab2da4
1,C:\Windows\System32\DriverStore\FileRepository\display.inf_amd64_neutral_ea1c8215e52777a6
1,C:\Windows\winsxs\x86_netfx-aspnet_rc_dll_res_b03f5f7f11d50a3a_6.1.7600.16385_none_04a12c6aba11825e
1,C:\Windows\winsxs\amd64_microsoft-windows-t..vice-core.resources_31bf3856ad364e35_6.1.7600.16385_en-us_2619acf06554ba90
1,C:\Windows\winsxs\amd64_netfx-aspnet_webadmin_wizard_b03f5f7f11d50a3a_6.1.7600.16385_none_f3ab6fef34443b5c
1,C:\Windows\assembly\NativeImages_v2.0.50727_32\AuditPolicyGPManage#\a0a453714c9ec8d6954490f711f5158a
1,C:\Windows\winsxs\amd64_hpoa1so.inf_31bf3856ad364e35_6.1.7600.16385_none_9f729ae40a99fd9d
4,Windows Only


'''
