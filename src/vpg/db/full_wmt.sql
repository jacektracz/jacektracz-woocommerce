-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 17, 2017 at 12:14 AM
-- Server version: 5.7.16-log
-- PHP Version: 7.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wmt`
--

-- --------------------------------------------------------

--
-- Table structure for table `bertas`
--

CREATE TABLE `bertas` (
  `id` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `location` text COLLATE utf8_unicode_ci,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `bertas`
--

INSERT INTO `bertas` (`id`, `changed_by`, `created_by`, `revision`, `label`, `location`, `created_at`, `changed_at`, `hash`) VALUES
(5, 1, 1, NULL, '1', NULL, 1, 2, '$epgenberta$782bcfb847a0ff5db5cc74b4d6817c40de623415189a805e31e90db37a3675e1'),
(6, 1, 1, NULL, 'az', '1', 1484468148, 1484468148, '$xpgenbertasxitem$d9fe8c36d3454f60a4655d2d78e55447ee33e9e47f2efe5112a59e7630c2cae4'),
(7, 1, 1, NULL, 'aa', 'aa', 1484775319, 1484775319, '$xpgenbertasxitem$5a4ec6046f260f6dd5a02c108037f5eb3f54a41cd8e51c0e0f42e069b6f139b8'),
(8, 1, 1, NULL, 'laabel', 'laabel', 1484775509, 1484775509, '$xpgenbertasxitem$aa8e089329d7ac5dfe8fecdd1793a903665faa135bff95bcbc859a3321a8b637'),
(9, 1, 1, NULL, 'jki', 'jki', 1484807338, 1484807338, '$xpgenbertasxitem$2e874f29133598e86e5c80ac150c3acc86b1f2c10ddf5870e1c86d9389bac317'),
(10, 1, 1, NULL, 'bbbbb', 'b', 1485003228, 1485003228, '$xpgenbertasxitem$7a909e70575a4d4b00a4cf480c4a87f42fd99507a7ac986308f58b1d83b56a02'),
(11, 1, 1, NULL, 'bbbbb', 'b', 1485003233, 1485003233, '$xpgenbertasxitem$7ab351f82cd36ac97a2f9cde1149c42c6fef5c51bbe2f02bac1218456551b7b1'),
(12, 8011, 1, NULL, '1eee', '1eee', 1485003259, 1486948296, '$xpgenbertasxitem$926cf5dab3eb4ea0ebc44e6173caa24b8ae206b61382971da08b913f5bbd85bd');

-- --------------------------------------------------------

--
-- Table structure for table `configurations`
--

CREATE TABLE `configurations` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `description` text CHARACTER SET latin1,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `ctx` varchar(50) NOT NULL,
  `ctxid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `configurations`
--

INSERT INTO `configurations` (`id`, `label`, `description`, `created_at`, `changed_at`, `created_by`, `changed_by`, `hash`, `revision`, `ctx`, `ctxid`) VALUES
(186, 'config-1', NULL, 1, 1, 1, 1, '$xpgenconfigurationsxitem$f10e662ec3e7aa71f833084eacbf5b0ab0f250138822f37de3a1431b24c6930a', NULL, '1', 1),
(187, 'config-2', NULL, 1, 1, 1, 1, '$xpgenconfigurationsxitem$a0120042adb5f095ad9782a9fed5e1aa817a2bcd130f4cc559d2870f199b30af', NULL, '1', 1),
(188, 'aaaa', 'vvvvv', 1483576450, 1483576450, 1, 1, '$xpgenconfigurationsxitem$6f9303dc3c422b398d9002ab9301eec9d78b3973f4063a430d0a7d80003f824b', NULL, '1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `configuration_fields`
--

CREATE TABLE `configuration_fields` (
  `id` int(11) NOT NULL,
  `configuration` int(11) DEFAULT NULL,
  `fieldname` varchar(50) NOT NULL,
  `fieldvalue` varchar(200) NOT NULL,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `doctrine_migration_versions`
--

CREATE TABLE `doctrine_migration_versions` (
  `version` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `operation_system`
--

CREATE TABLE `operation_system` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `version` varchar(20) NOT NULL,
  `family_id` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `osfamily`
--

CREATE TABLE `osfamily` (
  `id` int(11) NOT NULL,
  `family` varchar(20) NOT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `osfamily`
--

INSERT INTO `osfamily` (`id`, `family`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `revision`) VALUES
(1, '1', '1', 1, 1, 1, 1, 1),
(2, 'os 1', '$xpgenosfamilyxitem$ddd1dcbbc3144182b925a714fd6db642d2c331fd84879af460e9b150e4c746c4', 1484468873, 1, 1484468873, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `os_api`
--

CREATE TABLE `os_api` (
  `id` int(11) NOT NULL,
  `label` varchar(50) NOT NULL,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `osfamily` int(11) DEFAULT NULL,
  `version` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `os_api`
--

INSERT INTO `os_api` (`id`, `label`, `created_at`, `changed_at`, `created_by`, `changed_by`, `hash`, `revision`, `osfamily`, `version`) VALUES
(15, 'osapi-1', 1, 1, 1, 1, '$xpgenos_apixitem$c55a503aa201b1c89cdf385a7b27b727753072dbfbbc4c17d28235621b94088b', NULL, 1, '1'),
(16, 'osapi-2', 1, 1483576174, 1, 1, '$xpgenos_apixitem$2498d50cef4929f0579430f8069c23ce6ebd1bd4f196690016f398ae89f99def', NULL, 1, '1'),
(17, '1', 1483336683, 1483336683, 1, 1, '$xpgenos_apixitem$3c34d383107ee1083398304dea914029d5af76cc7511f5deb6c3a2038f34deca', NULL, 1, '12'),
(18, 'asd', 1483576200, 1483576213, 1, 1, '$xpgenos_apixitem$88d7cc03c726ad239362e7e656ac7877e36998b2323a5c0c8e05f004f17b64ac', NULL, NULL, '12'),
(19, 'aaaakkkk', 1485215306, 1485215306, 1, 1, '$xpgenos_apixitem$3a9e43f848ec8435719ab1edd65ec4114962204c8a2f699afe5140ccd3eb1bea', NULL, 2, '12');

-- --------------------------------------------------------

--
-- Table structure for table `platforms`
--

CREATE TABLE `platforms` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `platforms`
--

INSERT INTO `platforms` (`id`, `name`, `created_at`, `created_by`, `changed_at`, `changed_by`, `revision`, `hash`) VALUES
(13, 'platform-name', 1, 1, 1, 1, NULL, '$xpgenplatformsxitem$b8912ec8f84b70fd392863faa68e3e7f3ec109bdc055192db80006fedcd81602'),
(14, 'a1', 1485216622, 1, 1485216622, 1, NULL, '$xpgenplatformsxitem$ba575f4a9f356779d53a25b0315bf487b4a92387bd8b5324135c1110014c7a9a');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `submitted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `label`, `created_at`, `created_by`, `changed_at`, `changed_by`, `hash`, `revision`, `submitted`) VALUES
(1, '1', 1, 1, 1, 1, '1', 1, 1),
(30, 'project-2', 1, 1, 1, 1, '$xpgenprojectsxitem$741b907779d865e61186af1af5066468a390031ea4f4b8c5f184a99daff4c054', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `projects_streams`
--

CREATE TABLE `projects_streams` (
  `stream` int(11) NOT NULL,
  `project` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projects_streams`
--

INSERT INTO `projects_streams` (`stream`, `project`, `id`) VALUES
(4, 30, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `projects_workloads`
--

CREATE TABLE `projects_workloads` (
  `workload` int(11) DEFAULT NULL,
  `project` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projects_workloads`
--

INSERT INTO `projects_workloads` (`workload`, `project`, `id`) VALUES
(123, 30, 35),
(123, 30, 36),
(123, 30, 37),
(123, 30, 38),
(123, 30, 39),
(123, 30, 40),
(123, 30, 41),
(123, 30, 42),
(123, 30, 43),
(123, 30, 44),
(122, 30, 45),
(122, 30, 46),
(122, 30, 47),
(122, 30, 48),
(122, 30, 49),
(122, 30, 50),
(122, 30, 51),
(123, NULL, 52);

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `id` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `assigned_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `body` longtext,
  `rqbody` longtext,
  `rgactions` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `rgqueuesend` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `rgcsvimport` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`id`, `status`, `created_at`, `changed_at`, `assigned_at`, `created_by`, `changed_by`, `assignedTo`, `hash`, `revision`, `type`, `body`, `rqbody`, `rgactions`, `rgqueuesend`, `rgcsvimport`) VALUES
(1393, NULL, 1483294132, 1483294132, 1, 1, 1, NULL, '$xpgenrequestxitem$a79fc333502a54d82f07e8ae617091d8bb626ba159c45a247e12222b71e48c5e', NULL, 36, '1', '1', NULL, NULL, NULL),
(1395, NULL, 1484204217, 1484204217, NULL, 1, 1, NULL, '$xpgenrequestxitem$3f068387eccf14cfa9e833b2f765cdf8f92571957c76a5722a02693b200d8ebb', NULL, 39, '{"test_data":{"stream_id":"","stream_hash":"","stream_fullName":"","berta_id":"","berta_hash":"","berta_label":"","berta_scenario":"","test_label":"ggg","test_comment":"","scenario_comment":"","title_id":"","title_hash":"","title_label":"","is_gta":"","frame_from":0,"frame_to":0,"rqpriority_hash":"","rqpriority_label":"","rqpriority_id":"","subtype_hash":"","subtype_label":"","subtype_id":"","rqstatus_hash":"","rqstatus_id":"","rqstatus_label":"","rquser_id":"","rquser_hash":"","rquser_label":"","last_field":"last-field-id"},"stream_data":{"stream_id":"","stream_hash":"","stream_fullName":"","title_id":"","title_hash":"","title_label":"","titleversion_id":"","titleversion_hash":"","titleversion_label":"","titlescenario_id":"","titlescenario_hash":"","titlescenario_label":"","osapi_id":"","osapi_hash":"","osapi_label":"","configuration_id":"","configuration_hash":"","configuration_label":"","platform_id":"","platform_hash":"","platform_label":"","stream_file_binary":"","new_title":"","new_version":"","new_scenario":"","new_api":"","new_configuration":"","new_platform":"","last_field_stream":"last-field-id"},"rq_type":"stream_and_test"}', NULL, NULL, NULL, NULL),
(1396, NULL, 1484204408, 1484204408, NULL, 1, 1, NULL, '$xpgenrequestxitem$422f506c95ac740e25addc26c12896cca406a709494a6be1f37db0a53bf1945a', NULL, 39, '{"test_data":{"stream_id":"","stream_hash":"","stream_fullName":"","berta_id":"","berta_hash":"","berta_label":"","berta_scenario":"","test_label":"ggg-2","test_comment":"","scenario_comment":"","title_id":"","title_hash":"","title_label":"","is_gta":"","frame_from":0,"frame_to":0,"rqpriority_hash":"","rqpriority_label":"","rqpriority_id":"","subtype_hash":"","subtype_label":"","subtype_id":"","rqstatus_hash":"","rqstatus_id":"","rqstatus_label":"","rquser_id":"","rquser_hash":"","rquser_label":"","last_field":"last-field-id"},"stream_data":{"stream_id":"","stream_hash":"","stream_fullName":"","title_id":"","title_hash":"","title_label":"","titleversion_id":"","titleversion_hash":"","titleversion_label":"","titlescenario_id":"","titlescenario_hash":"","titlescenario_label":"","osapi_id":"","osapi_hash":"","osapi_label":"","configuration_id":"","configuration_hash":"","configuration_label":"","platform_id":"","platform_hash":"","platform_label":"","stream_file_binary":"","new_title":"","new_version":"","new_scenario":"","new_api":"","new_configuration":"","new_platform":"","last_field_stream":"last-field-id"},"rq_type":"stream_and_test"}', NULL, NULL, NULL, NULL),
(1397, NULL, 1484635500, 1484635500, NULL, 1, 1, NULL, '$xpgenrequestxitem$8002cec995c2e53417fb34612cfcf8e7801200dd518d477a9fbb1f1f7609b66b', NULL, 39, NULL, NULL, NULL, NULL, NULL),
(1398, NULL, 1485691700, 1486896020, NULL, 8011, 8011, NULL, '$xpgenrequestxitem$595fb6df64df7411d01d35f05de4df8f44c27904a2133fa179b69f27b3b0e16c', NULL, 39, NULL, NULL, NULL, '0', NULL),
(1399, NULL, 1486896064, 1486896064, NULL, 8011, 8011, NULL, '$xpgenrequestxitem$7f12ec26552662a54ddffb70a95bab32978dd2ba3dc3ea0aa532bfe6e9a6f68d', NULL, 39, NULL, NULL, NULL, '0', NULL),
(1400, NULL, 1486896996, 1486897036, NULL, 8011, 8011, NULL, '$xpgenrequestxitem$ff8923b0385a3d33576058a2b960f4dab424d5ffb0646a83833ab5e0f4ba664b', NULL, 39, NULL, NULL, NULL, '0', NULL),
(1401, NULL, 1487286885, 1487286885, NULL, 8011, 8011, NULL, '$xpgenrequestxitem$31d8cfd51988023e5a2db551808a6b5da14573468f29e100fc6843ea995b2a22', NULL, 39, NULL, NULL, NULL, '0', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rqdefcolumn`
--

CREATE TABLE `rqdefcolumn` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqactions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqitemtype` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqdefview_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqdefcolumn`
--

INSERT INTO `rqdefcolumn` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqkey`, `rqvalue`, `rqstatus`, `rqactions`, `rqitemtype`, `rqdefview_id`) VALUES
(121, 'genf_hash', 'genf_hash', NULL, '$xpgenrqdefcolumnxitem$f12af25f63294b406eef97f3d7aa877d42fc59914566dfcb91013312251d7945', 1485899622, 8012, 1485899622, 8012, NULL, 'genf_hash', '1', NULL, NULL, '1', 121);

-- --------------------------------------------------------

--
-- Table structure for table `rqdefview`
--

CREATE TABLE `rqdefview` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqactions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqitemtype` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqdefview`
--

INSERT INTO `rqdefview` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqkey`, `rqvalue`, `rqstatus`, `rqactions`, `rqitemtype`) VALUES
(121, 'jxpgenconfigurationsxitem', 'jxpgenconfigurationsxitem', NULL, '$xpgenrqdefviewxitem$94fe7803252895af3604fb516625cd9a1e6ec61fa437d5d6a218241b2b9e76aa', 1485899512, 8012, 1485899512, 8012, NULL, 'jxpgenconfigurationsxitem', '1', NULL, NULL, '1');

-- --------------------------------------------------------

--
-- Table structure for table `rqpriority`
--

CREATE TABLE `rqpriority` (
  `id` int(11) NOT NULL,
  `label` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rqpriority`
--

INSERT INTO `rqpriority` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`) VALUES
(50, 'prio-1', 'slug-1', NULL, '$xpgenrqpriorityxitem$9969875fc469ab800a5e4bb86fe9b2505187360b4d95cfbe0fd8364e69a16316', 1, 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `rqrole`
--

CREATE TABLE `rqrole` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqroletype_id` int(11) DEFAULT NULL,
  `rqtypekey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqrole`
--

INSERT INTO `rqrole` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqroletype_id`, `rqtypekey`, `rqkey`, `rqvalue`) VALUES
(1, '1', '1', NULL, '$xpgenrqrolexitem$bfd6cc6786a4df51d3e4e3914f24cdde6ff5086dc6061fda87c870d2f9afa1b7', 1485477071, 1, 1485477071, 1, NULL, NULL, NULL, NULL, NULL),
(2, 'scateadmin', 'scateadmin', NULL, '$xpgenrqrolexitem$8c9783b9bb60f2a8d55e1fc1f86fb4c4ba18f99c7b961811f1ebef56d2435dc9', 1486808249, 8011, 1486808249, 8011, NULL, NULL, NULL, 'scateadmin', 'scateadmin');

-- --------------------------------------------------------

--
-- Table structure for table `rqrole_status`
--

CREATE TABLE `rqrole_status` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqactions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rgrole_id` int(11) DEFAULT NULL,
  `rqstatus_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqrole_status`
--

INSERT INTO `rqrole_status` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqkey`, `rqvalue`, `rqstatus`, `rqactions`, `rgrole_id`, `rqstatus_id`) VALUES
(120, NULL, NULL, NULL, '$xpgenrqrole_statusxitem$a7c912f4fc3c3ef9f98b4770cb9a0cba534bb75268e4d67114bd3529220112a0', 1485477086, 1, 1485477086, 1, NULL, NULL, NULL, NULL, NULL, 1, NULL),
(121, '1', '1', NULL, '$xpgenrqrole_statusxitem$b8f559b06d439a123e8186a1fc35819183c71b7ba1941bbc3520669d7f273aef', 1485479397, 1, 1485596656, 1, NULL, NULL, NULL, NULL, NULL, 1, 25);

-- --------------------------------------------------------

--
-- Table structure for table `rqscimp`
--

CREATE TABLE `rqscimp` (
  `id` int(11) NOT NULL,
  `label` text COLLATE utf8_unicode_ci,
  `slug` text COLLATE utf8_unicode_ci,
  `revision` int(11) DEFAULT NULL,
  `hash` text COLLATE utf8_unicode_ci,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `berta_id` int(11) DEFAULT NULL,
  `title_id` int(11) DEFAULT NULL,
  `titleversion_id` int(11) DEFAULT NULL,
  `titlescenario_id` int(11) DEFAULT NULL,
  `osapi_id` int(11) DEFAULT NULL,
  `configuration_id` int(11) DEFAULT NULL,
  `platform_id` int(11) DEFAULT NULL,
  `rqpriority_id` int(11) DEFAULT NULL,
  `subtype_id` int(11) DEFAULT NULL,
  `rqsctest_id` int(11) DEFAULT NULL,
  `rquser_id` int(11) DEFAULT NULL,
  `is_gta` int(11) DEFAULT NULL,
  `frame_form` int(11) DEFAULT NULL,
  `frame_to` int(11) DEFAULT NULL,
  `stream_id` int(11) DEFAULT NULL,
  `new_title` text COLLATE utf8_unicode_ci,
  `new_version` text COLLATE utf8_unicode_ci,
  `new_scenario` text COLLATE utf8_unicode_ci,
  `new_api` text COLLATE utf8_unicode_ci,
  `new_configuration` text COLLATE utf8_unicode_ci,
  `new_platform` text COLLATE utf8_unicode_ci,
  `request_id` int(11) DEFAULT NULL,
  `rq_type` int(11) DEFAULT NULL,
  `rqbody` longtext COLLATE utf8_unicode_ci,
  `rqcomment` longtext COLLATE utf8_unicode_ci,
  `berta_scenario` text COLLATE utf8_unicode_ci,
  `api_trace` text COLLATE utf8_unicode_ci,
  `rqstatus_id` int(11) DEFAULT NULL,
  `apitrace_path` text COLLATE utf8_unicode_ci,
  `rqtest_id` int(11) DEFAULT NULL,
  `rqdesc` text COLLATE utf8_unicode_ci,
  `trace_path` text COLLATE utf8_unicode_ci,
  `manifest_path` text COLLATE utf8_unicode_ci,
  `owner` text COLLATE utf8_unicode_ci,
  `trace_write_date` text COLLATE utf8_unicode_ci,
  `is_path_correct` text COLLATE utf8_unicode_ci,
  `is_path_wospaces` text COLLATE utf8_unicode_ci,
  `is_path_wounderlines` text COLLATE utf8_unicode_ci,
  `is_path_wodots` text COLLATE utf8_unicode_ci,
  `is_streamname_correct` text COLLATE utf8_unicode_ci,
  `is_api_correct` text COLLATE utf8_unicode_ci,
  `is_prefix_correct` text COLLATE utf8_unicode_ci,
  `is_os_correct` text COLLATE utf8_unicode_ci,
  `is_attribini_found` text COLLATE utf8_unicode_ci,
  `is_screenshots_dir_correct` text COLLATE utf8_unicode_ci,
  `is_everything_correct` text COLLATE utf8_unicode_ci,
  `is_attribini_correct` text COLLATE utf8_unicode_ci,
  `test_name` text COLLATE utf8_unicode_ci,
  `testsuite_framestart` text COLLATE utf8_unicode_ci,
  `testsuite_framecount` text COLLATE utf8_unicode_ci,
  `testsuite_framestep` text COLLATE utf8_unicode_ci,
  `testsuite_tolerance` text COLLATE utf8_unicode_ci,
  `testsuite_demo` text COLLATE utf8_unicode_ci,
  `testsuite_gameproperties` text COLLATE utf8_unicode_ci,
  `testsuite_referencedir` text COLLATE utf8_unicode_ci,
  `testsuite_dumpdir` text COLLATE utf8_unicode_ci,
  `testsuite_comparer` text COLLATE utf8_unicode_ci,
  `testsuite_comparerargs` text COLLATE utf8_unicode_ci,
  `testsuite_version` text COLLATE utf8_unicode_ci,
  `testsuite_mask` text COLLATE utf8_unicode_ci,
  `testsuite_selected` text COLLATE utf8_unicode_ci,
  `testsuite_pave_sb` text COLLATE utf8_unicode_ci,
  `testsuite_drawcallmode` text COLLATE utf8_unicode_ci,
  `testsuite_maskrandom` text COLLATE utf8_unicode_ci,
  `testsuite_nulldriver` text COLLATE utf8_unicode_ci,
  `testsuite_imola` text COLLATE utf8_unicode_ci,
  `testsuite_emulate` text COLLATE utf8_unicode_ci,
  `testsuite_pave_tv` text COLLATE utf8_unicode_ci,
  `testsuite_nullhw` text COLLATE utf8_unicode_ci,
  `testsuite_nullkmd` text COLLATE utf8_unicode_ci,
  `testsuite_game` text COLLATE utf8_unicode_ci,
  `testsuite_scenario` text COLLATE utf8_unicode_ci,
  `testsuite_createdwithscateversion` text COLLATE utf8_unicode_ci,
  `testsuite_playercapturearg` text COLLATE utf8_unicode_ci,
  `testsuite_screenshotsformat` text COLLATE utf8_unicode_ci,
  `testsuite_ignoredframes` text COLLATE utf8_unicode_ci,
  `basics_frames_count_used` text COLLATE utf8_unicode_ci,
  `basics_frames_count_created` text COLLATE utf8_unicode_ci,
  `basics_draw_calls_count_used` text COLLATE utf8_unicode_ci,
  `basics_draw_calls_count_created` text COLLATE utf8_unicode_ci,
  `basics_resolution_used` text COLLATE utf8_unicode_ci,
  `basics_resolution_created` text COLLATE utf8_unicode_ci,
  `basics_swapchain_formats_used` text COLLATE utf8_unicode_ci,
  `basics_swapchain_formats_created` text COLLATE utf8_unicode_ci,
  `basics_texture_1d_used` text COLLATE utf8_unicode_ci,
  `basics_texture_1d_created` text COLLATE utf8_unicode_ci,
  `basics_texture_2d_used` text COLLATE utf8_unicode_ci,
  `basics_texture_2d_created` text COLLATE utf8_unicode_ci,
  `basics_texture_3d_used` text COLLATE utf8_unicode_ci,
  `basics_texture_3d_created` text COLLATE utf8_unicode_ci,
  `basics_fullscreen_msaa_used` text COLLATE utf8_unicode_ci,
  `basics_fullscreen_msaa_created` text COLLATE utf8_unicode_ci,
  `basics_msaa_usedbasics_msaa_created` text COLLATE utf8_unicode_ci,
  `basics__usedbasics__created` text COLLATE utf8_unicode_ci,
  `basics_textures_formats_used` text COLLATE utf8_unicode_ci,
  `basics_textures_formats_created` text COLLATE utf8_unicode_ci,
  `dx9_vertex_shader_used` text COLLATE utf8_unicode_ci,
  `dx9_vertex_shader_created` text COLLATE utf8_unicode_ci,
  `dx9_pixel_shader_used` text COLLATE utf8_unicode_ci,
  `dx9_pixel_shader_created` text COLLATE utf8_unicode_ci,
  `dx9_null_render_target_used` text COLLATE utf8_unicode_ci,
  `dx9_null_render_target_created` text COLLATE utf8_unicode_ci,
  `dx9_ati1n_used` text COLLATE utf8_unicode_ci,
  `dx9_ati1n_created` text COLLATE utf8_unicode_ci,
  `dx9_ati2n_used` text COLLATE utf8_unicode_ci,
  `dx9_ati2n_created` text COLLATE utf8_unicode_ci,
  `dx9_intz_used` text COLLATE utf8_unicode_ci,
  `dx9_intz_created` text COLLATE utf8_unicode_ci,
  `dx9_rawz_used` text COLLATE utf8_unicode_ci,
  `dx9_rawz_created` text COLLATE utf8_unicode_ci,
  `dx9_df16_used` text COLLATE utf8_unicode_ci,
  `dx9_df16_created` text COLLATE utf8_unicode_ci,
  `dx9_df24_used` text COLLATE utf8_unicode_ci,
  `dx9_df24_created` text COLLATE utf8_unicode_ci,
  `dx9_nvdb_used` text COLLATE utf8_unicode_ci,
  `dx9_nvdb_created` text COLLATE utf8_unicode_ci,
  `dx9_resz_used` text COLLATE utf8_unicode_ci,
  `dx9_resz_created` text COLLATE utf8_unicode_ci,
  `dx9_atoc_used` text COLLATE utf8_unicode_ci,
  `dx9_atoc_created` text COLLATE utf8_unicode_ci,
  `dx9_ssaa_used` text COLLATE utf8_unicode_ci,
  `dx9_ssaa_created` text COLLATE utf8_unicode_ci,
  `dx9_ati_atoc_used` text COLLATE utf8_unicode_ci,
  `dx9_ati_atoc_created` text COLLATE utf8_unicode_ci,
  `dx9_fetch4_used` text COLLATE utf8_unicode_ci,
  `dx9_fetch4_created` text COLLATE utf8_unicode_ci,
  `dx9_cube_maps_used` text COLLATE utf8_unicode_ci,
  `dx9_cube_maps_created` text COLLATE utf8_unicode_ci,
  `dx9_cube_maps_formats_used` text COLLATE utf8_unicode_ci,
  `dx9_cube_maps_formats_created` text COLLATE utf8_unicode_ci,
  `dx9_volumetric_surfaces_used` text COLLATE utf8_unicode_ci,
  `dx9_volumetric_surfaces_created` text COLLATE utf8_unicode_ci,
  `dx9_volumetric_surfaces_formats_used` text COLLATE utf8_unicode_ci,
  `dx9_volumetric_surfaces_formats_created` text COLLATE utf8_unicode_ci,
  `dx9_anizotropic_filtration_used` text COLLATE utf8_unicode_ci,
  `dx9_anizotropic_filtration_created` text COLLATE utf8_unicode_ci,
  `dx10_vertex_shader_used` text COLLATE utf8_unicode_ci,
  `dx10_vertex_shader_created` text COLLATE utf8_unicode_ci,
  `dx10_pixel_shader_used` text COLLATE utf8_unicode_ci,
  `dx10_pixel_shader_created` text COLLATE utf8_unicode_ci,
  `dx10__used` text COLLATE utf8_unicode_ci,
  `dx10__created` text COLLATE utf8_unicode_ci,
  `dx10_geometry_shader_used` text COLLATE utf8_unicode_ci,
  `dx10_geometry_shader_created` text COLLATE utf8_unicode_ci,
  `dx10_resolve_subresource_used` text COLLATE utf8_unicode_ci,
  `dx10_resolve_subresource_created` text COLLATE utf8_unicode_ci,
  `dx10_draw_auto_used` text COLLATE utf8_unicode_ci,
  `dx10_draw_auto_created` text COLLATE utf8_unicode_ci,
  `dx10_gen_mipmaps_used` text COLLATE utf8_unicode_ci,
  `dx10_gen_mipmaps_created` text COLLATE utf8_unicode_ci,
  `dx10_gather4_used` text COLLATE utf8_unicode_ci,
  `dx10_gather4_created` text COLLATE utf8_unicode_ci,
  `dx10_cube_arrays_used` text COLLATE utf8_unicode_ci,
  `dx10_cube_arrays_created` text COLLATE utf8_unicode_ci,
  `dx11_vertex_shader_used` text COLLATE utf8_unicode_ci,
  `dx11_vertex_shader_created` text COLLATE utf8_unicode_ci,
  `dx11__useddx11__created` text COLLATE utf8_unicode_ci,
  `dx11_pixel_shader_used` text COLLATE utf8_unicode_ci,
  `dx11_pixel_shader_created` text COLLATE utf8_unicode_ci,
  `dx11_geometry_shader_used` text COLLATE utf8_unicode_ci,
  `dx11_geometry_shader_created` text COLLATE utf8_unicode_ci,
  `dx11_hull_shader_used` text COLLATE utf8_unicode_ci,
  `dx11_hull_shader_created` text COLLATE utf8_unicode_ci,
  `dx11_domain_shader_used` text COLLATE utf8_unicode_ci,
  `dx11_domain_shader_created` text COLLATE utf8_unicode_ci,
  `dx11_compute_shader_used` text COLLATE utf8_unicode_ci,
  `dx11_compute_shader_created` text COLLATE utf8_unicode_ci,
  `dx11_append_consume_used` text COLLATE utf8_unicode_ci,
  `dx11_append_consume_created` text COLLATE utf8_unicode_ci,
  `dx11_virtual_functions_used` text COLLATE utf8_unicode_ci,
  `dx11_virtual_functions_created` text COLLATE utf8_unicode_ci,
  `dx11_cube_arrays_used` text COLLATE utf8_unicode_ci,
  `dx11_cube_arrays_created` text COLLATE utf8_unicode_ci,
  `dx11_multithreading_used` text COLLATE utf8_unicode_ci,
  `dx11_multithreading_created` text COLLATE utf8_unicode_ci,
  `dx11_draw_auto_used` text COLLATE utf8_unicode_ci,
  `dx11_draw_auto_created` text COLLATE utf8_unicode_ci,
  `dx11_draw_indirect_used` text COLLATE utf8_unicode_ci,
  `dx11_draw_indirect_created` text COLLATE utf8_unicode_ci,
  `dx11_dispatch_used` text COLLATE utf8_unicode_ci,
  `dx11_dispatch_created` text COLLATE utf8_unicode_ci,
  `dx11_dispatch_indirect_used` text COLLATE utf8_unicode_ci,
  `dx11_dispatch_indirect_created` text COLLATE utf8_unicode_ci,
  `dx11_gather4_used` text COLLATE utf8_unicode_ci,
  `dx11_gather4_created` text COLLATE utf8_unicode_ci,
  `attrib_system_platform` text COLLATE utf8_unicode_ci,
  `attrib_system_device_description` text COLLATE utf8_unicode_ci,
  `attrib_system_chipset_version` text COLLATE utf8_unicode_ci,
  `attrib_system_os` text COLLATE utf8_unicode_ci,
  `attrib_system_os_version` text COLLATE utf8_unicode_ci,
  `attrib_system_driver_version` text COLLATE utf8_unicode_ci,
  `attrib_system_driver_version_qb` text COLLATE utf8_unicode_ci,
  `attrib_system_date` text COLLATE utf8_unicode_ci,
  `attrib_recorder_tool_name` text COLLATE utf8_unicode_ci,
  `attrib_recorder_tool_version` text COLLATE utf8_unicode_ci,
  `attrib_recorder_tool_bit_version` text COLLATE utf8_unicode_ci,
  `attrib_game_desiredoperatingsystem` text COLLATE utf8_unicode_ci,
  `attrib_game_category` text COLLATE utf8_unicode_ci,
  `attrib_game_subcategory` text COLLATE utf8_unicode_ci,
  `attrib_game_name` text COLLATE utf8_unicode_ci,
  `attrib_game_version` text COLLATE utf8_unicode_ci,
  `attrib_game_api` text COLLATE utf8_unicode_ci,
  `attrib_game_detail_level` text COLLATE utf8_unicode_ci,
  `attrib_game_resolution` text COLLATE utf8_unicode_ci,
  `attrib_game_gameengine` text COLLATE utf8_unicode_ci,
  `attrib_game_swgp_or_hwgp` text COLLATE utf8_unicode_ci,
  `attrib_game_menu_or_action` text COLLATE utf8_unicode_ci,
  `attrib_game_other_settings` text COLLATE utf8_unicode_ci,
  `attrib_other_frames_number` text COLLATE utf8_unicode_ci,
  `attrib_other_substream_range` text COLLATE utf8_unicode_ci,
  `attrib_other_known_problems` text COLLATE utf8_unicode_ci,
  `attrib_other_comments` text COLLATE utf8_unicode_ci,
  `attrib_replay_player` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerworkingdir` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerdir` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerexe` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerversion` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerargs` text COLLATE utf8_unicode_ci,
  `attrib_replay_gameoriginalexe` text COLLATE utf8_unicode_ci,
  `attrib_replay_playercapturefunction` text COLLATE utf8_unicode_ci,
  `attrib_system_os__2` text COLLATE utf8_unicode_ci,
  `attrib_game_workload` text COLLATE utf8_unicode_ci,
  `attrib_notes_note` text COLLATE utf8_unicode_ci,
  `attrib_other_frames_range` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_platform` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_device_description` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_chipset_version` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_os` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_os_version` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_driver_version` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_driver_version_qb` text COLLATE utf8_unicode_ci,
  `attrib_syapistem_date` text COLLATE utf8_unicode_ci,
  `attrib_other_subcapture` text COLLATE utf8_unicode_ci,
  `attrib_other_capture_command` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerexe2` text COLLATE utf8_unicode_ci,
  `attrib_replay_gameoriginalexe2` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerargs__2` text COLLATE utf8_unicode_ci,
  `attrib_system_gpu` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerdir__2` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerexe__2` text COLLATE utf8_unicode_ci,
  `attrib_replay_playercaption` text COLLATE utf8_unicode_ci,
  `attrib_replay_vrmode` text COLLATE utf8_unicode_ci,
  `attrib_game_vrmode` text COLLATE utf8_unicode_ci,
  `attrib_replay_d3d9device_number` text COLLATE utf8_unicode_ci,
  `attrib_replay_capture_method` text COLLATE utf8_unicode_ci,
  `attrib_compatibility_supportedgen` text COLLATE utf8_unicode_ci,
  `attrib_compatibility_unsupportedgen` text COLLATE utf8_unicode_ci,
  `attrib_compatibility_supportedos` text COLLATE utf8_unicode_ci,
  `attrib_compatibility_unsupportedos` text COLLATE utf8_unicode_ci,
  `attrib_other_subcapturerange` text COLLATE utf8_unicode_ci,
  `attrib_replay_gameoriginalexe_old` text COLLATE utf8_unicode_ci,
  `attrib_replay_playerargs_old` text COLLATE utf8_unicode_ci,
  `attrib_replay__gameoriginalexe` text COLLATE utf8_unicode_ci,
  `attrib__platform` text COLLATE utf8_unicode_ci,
  `attrib__device_description` text COLLATE utf8_unicode_ci,
  `attrib__chipset_version` text COLLATE utf8_unicode_ci,
  `attrib__os` text COLLATE utf8_unicode_ci,
  `attrib__driver_version` text COLLATE utf8_unicode_ci,
  `attrib__date` text COLLATE utf8_unicode_ci,
  `attrib_replay_environementvariables` text COLLATE utf8_unicode_ci,
  `attrib_missing` text COLLATE utf8_unicode_ci,
  `attrib_empty` text COLLATE utf8_unicode_ci,
  `attrib_wrong` text COLLATE utf8_unicode_ci,
  `trace_success` text COLLATE utf8_unicode_ci,
  `trace_d3d7` text COLLATE utf8_unicode_ci,
  `trace_d3d8` text COLLATE utf8_unicode_ci,
  `trace_d3d9` text COLLATE utf8_unicode_ci,
  `trace_d3d10` text COLLATE utf8_unicode_ci,
  `trace_d3d11` text COLLATE utf8_unicode_ci,
  `trace_d3d12` text COLLATE utf8_unicode_ci,
  `trace_dxgi` text COLLATE utf8_unicode_ci,
  `trace_direct2d` text COLLATE utf8_unicode_ci,
  `trace_directwrite` text COLLATE utf8_unicode_ci,
  `trace_opencl` text COLLATE utf8_unicode_ci,
  `trace_description` text COLLATE utf8_unicode_ci,
  `trace_driver_version` text COLLATE utf8_unicode_ci,
  `trace_vendor_id` text COLLATE utf8_unicode_ci,
  `trace_device_id` text COLLATE utf8_unicode_ci,
  `trace_subsys_id` text COLLATE utf8_unicode_ci,
  `trace_revision` text COLLATE utf8_unicode_ci,
  `trace_operating_system` text COLLATE utf8_unicode_ci,
  `trace_operating_system_label` text COLLATE utf8_unicode_ci,
  `trace_creation_data` text COLLATE utf8_unicode_ci,
  `trace_creation_time` text COLLATE utf8_unicode_ci,
  `trace_app_name` text COLLATE utf8_unicode_ci,
  `trace_computer_name` text COLLATE utf8_unicode_ci,
  `trace_idsid` text COLLATE utf8_unicode_ci,
  `trace_display_name` text COLLATE utf8_unicode_ci,
  `trace_gfx_bit_version` text COLLATE utf8_unicode_ci,
  `trace_framecount` text COLLATE utf8_unicode_ci,
  `trace_subcaptureframestart` text COLLATE utf8_unicode_ci,
  `trace_subcaptureframeend` text COLLATE utf8_unicode_ci,
  `rqscimp_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=COMPRESSED;

--
-- Dumping data for table `rqscimp`
--

INSERT INTO `rqscimp` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `berta_id`, `title_id`, `titleversion_id`, `titlescenario_id`, `osapi_id`, `configuration_id`, `platform_id`, `rqpriority_id`, `subtype_id`, `rqsctest_id`, `rquser_id`, `is_gta`, `frame_form`, `frame_to`, `stream_id`, `new_title`, `new_version`, `new_scenario`, `new_api`, `new_configuration`, `new_platform`, `request_id`, `rq_type`, `rqbody`, `rqcomment`, `berta_scenario`, `api_trace`, `rqstatus_id`, `apitrace_path`, `rqtest_id`, `rqdesc`, `trace_path`, `manifest_path`, `owner`, `trace_write_date`, `is_path_correct`, `is_path_wospaces`, `is_path_wounderlines`, `is_path_wodots`, `is_streamname_correct`, `is_api_correct`, `is_prefix_correct`, `is_os_correct`, `is_attribini_found`, `is_screenshots_dir_correct`, `is_everything_correct`, `is_attribini_correct`, `test_name`, `testsuite_framestart`, `testsuite_framecount`, `testsuite_framestep`, `testsuite_tolerance`, `testsuite_demo`, `testsuite_gameproperties`, `testsuite_referencedir`, `testsuite_dumpdir`, `testsuite_comparer`, `testsuite_comparerargs`, `testsuite_version`, `testsuite_mask`, `testsuite_selected`, `testsuite_pave_sb`, `testsuite_drawcallmode`, `testsuite_maskrandom`, `testsuite_nulldriver`, `testsuite_imola`, `testsuite_emulate`, `testsuite_pave_tv`, `testsuite_nullhw`, `testsuite_nullkmd`, `testsuite_game`, `testsuite_scenario`, `testsuite_createdwithscateversion`, `testsuite_playercapturearg`, `testsuite_screenshotsformat`, `testsuite_ignoredframes`, `basics_frames_count_used`, `basics_frames_count_created`, `basics_draw_calls_count_used`, `basics_draw_calls_count_created`, `basics_resolution_used`, `basics_resolution_created`, `basics_swapchain_formats_used`, `basics_swapchain_formats_created`, `basics_texture_1d_used`, `basics_texture_1d_created`, `basics_texture_2d_used`, `basics_texture_2d_created`, `basics_texture_3d_used`, `basics_texture_3d_created`, `basics_fullscreen_msaa_used`, `basics_fullscreen_msaa_created`, `basics_msaa_usedbasics_msaa_created`, `basics__usedbasics__created`, `basics_textures_formats_used`, `basics_textures_formats_created`, `dx9_vertex_shader_used`, `dx9_vertex_shader_created`, `dx9_pixel_shader_used`, `dx9_pixel_shader_created`, `dx9_null_render_target_used`, `dx9_null_render_target_created`, `dx9_ati1n_used`, `dx9_ati1n_created`, `dx9_ati2n_used`, `dx9_ati2n_created`, `dx9_intz_used`, `dx9_intz_created`, `dx9_rawz_used`, `dx9_rawz_created`, `dx9_df16_used`, `dx9_df16_created`, `dx9_df24_used`, `dx9_df24_created`, `dx9_nvdb_used`, `dx9_nvdb_created`, `dx9_resz_used`, `dx9_resz_created`, `dx9_atoc_used`, `dx9_atoc_created`, `dx9_ssaa_used`, `dx9_ssaa_created`, `dx9_ati_atoc_used`, `dx9_ati_atoc_created`, `dx9_fetch4_used`, `dx9_fetch4_created`, `dx9_cube_maps_used`, `dx9_cube_maps_created`, `dx9_cube_maps_formats_used`, `dx9_cube_maps_formats_created`, `dx9_volumetric_surfaces_used`, `dx9_volumetric_surfaces_created`, `dx9_volumetric_surfaces_formats_used`, `dx9_volumetric_surfaces_formats_created`, `dx9_anizotropic_filtration_used`, `dx9_anizotropic_filtration_created`, `dx10_vertex_shader_used`, `dx10_vertex_shader_created`, `dx10_pixel_shader_used`, `dx10_pixel_shader_created`, `dx10__used`, `dx10__created`, `dx10_geometry_shader_used`, `dx10_geometry_shader_created`, `dx10_resolve_subresource_used`, `dx10_resolve_subresource_created`, `dx10_draw_auto_used`, `dx10_draw_auto_created`, `dx10_gen_mipmaps_used`, `dx10_gen_mipmaps_created`, `dx10_gather4_used`, `dx10_gather4_created`, `dx10_cube_arrays_used`, `dx10_cube_arrays_created`, `dx11_vertex_shader_used`, `dx11_vertex_shader_created`, `dx11__useddx11__created`, `dx11_pixel_shader_used`, `dx11_pixel_shader_created`, `dx11_geometry_shader_used`, `dx11_geometry_shader_created`, `dx11_hull_shader_used`, `dx11_hull_shader_created`, `dx11_domain_shader_used`, `dx11_domain_shader_created`, `dx11_compute_shader_used`, `dx11_compute_shader_created`, `dx11_append_consume_used`, `dx11_append_consume_created`, `dx11_virtual_functions_used`, `dx11_virtual_functions_created`, `dx11_cube_arrays_used`, `dx11_cube_arrays_created`, `dx11_multithreading_used`, `dx11_multithreading_created`, `dx11_draw_auto_used`, `dx11_draw_auto_created`, `dx11_draw_indirect_used`, `dx11_draw_indirect_created`, `dx11_dispatch_used`, `dx11_dispatch_created`, `dx11_dispatch_indirect_used`, `dx11_dispatch_indirect_created`, `dx11_gather4_used`, `dx11_gather4_created`, `attrib_system_platform`, `attrib_system_device_description`, `attrib_system_chipset_version`, `attrib_system_os`, `attrib_system_os_version`, `attrib_system_driver_version`, `attrib_system_driver_version_qb`, `attrib_system_date`, `attrib_recorder_tool_name`, `attrib_recorder_tool_version`, `attrib_recorder_tool_bit_version`, `attrib_game_desiredoperatingsystem`, `attrib_game_category`, `attrib_game_subcategory`, `attrib_game_name`, `attrib_game_version`, `attrib_game_api`, `attrib_game_detail_level`, `attrib_game_resolution`, `attrib_game_gameengine`, `attrib_game_swgp_or_hwgp`, `attrib_game_menu_or_action`, `attrib_game_other_settings`, `attrib_other_frames_number`, `attrib_other_substream_range`, `attrib_other_known_problems`, `attrib_other_comments`, `attrib_replay_player`, `attrib_replay_playerworkingdir`, `attrib_replay_playerdir`, `attrib_replay_playerexe`, `attrib_replay_playerversion`, `attrib_replay_playerargs`, `attrib_replay_gameoriginalexe`, `attrib_replay_playercapturefunction`, `attrib_system_os__2`, `attrib_game_workload`, `attrib_notes_note`, `attrib_other_frames_range`, `attrib_syapistem_platform`, `attrib_syapistem_device_description`, `attrib_syapistem_chipset_version`, `attrib_syapistem_os`, `attrib_syapistem_os_version`, `attrib_syapistem_driver_version`, `attrib_syapistem_driver_version_qb`, `attrib_syapistem_date`, `attrib_other_subcapture`, `attrib_other_capture_command`, `attrib_replay_playerexe2`, `attrib_replay_gameoriginalexe2`, `attrib_replay_playerargs__2`, `attrib_system_gpu`, `attrib_replay_playerdir__2`, `attrib_replay_playerexe__2`, `attrib_replay_playercaption`, `attrib_replay_vrmode`, `attrib_game_vrmode`, `attrib_replay_d3d9device_number`, `attrib_replay_capture_method`, `attrib_compatibility_supportedgen`, `attrib_compatibility_unsupportedgen`, `attrib_compatibility_supportedos`, `attrib_compatibility_unsupportedos`, `attrib_other_subcapturerange`, `attrib_replay_gameoriginalexe_old`, `attrib_replay_playerargs_old`, `attrib_replay__gameoriginalexe`, `attrib__platform`, `attrib__device_description`, `attrib__chipset_version`, `attrib__os`, `attrib__driver_version`, `attrib__date`, `attrib_replay_environementvariables`, `attrib_missing`, `attrib_empty`, `attrib_wrong`, `trace_success`, `trace_d3d7`, `trace_d3d8`, `trace_d3d9`, `trace_d3d10`, `trace_d3d11`, `trace_d3d12`, `trace_dxgi`, `trace_direct2d`, `trace_directwrite`, `trace_opencl`, `trace_description`, `trace_driver_version`, `trace_vendor_id`, `trace_device_id`, `trace_subsys_id`, `trace_revision`, `trace_operating_system`, `trace_operating_system_label`, `trace_creation_data`, `trace_creation_time`, `trace_app_name`, `trace_computer_name`, `trace_idsid`, `trace_display_name`, `trace_gfx_bit_version`, `trace_framecount`, `trace_subcaptureframestart`, `trace_subcaptureframeend`, `rqscimp_id`) VALUES
(120, '1', '1', NULL, '$xpgenrqscimpxitem$91c307f6d079eb97b484a662b9fe7780d00e644226e63b31c71d7edd45295f45', 1484987678, 1, 1484987678, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `rqscimport`
--

CREATE TABLE `rqscimport` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rq_imp_status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_imp_class` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_imp_type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_imp_from` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_imp_to` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_imp_count` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_imp_test` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqscimport`
--

INSERT INTO `rqscimport` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rq_imp_status`, `rq_imp_class`, `rq_imp_type`, `rq_imp_from`, `rq_imp_to`, `rq_imp_count`, `rq_imp_test`) VALUES
(120, '1', '1', NULL, '$xpgenrqscimportxitem$3d62bb71baaa5260ca0bfe31a8474d27da909bff06f913d6c50bf7cb41fb9098', 1485331072, 1, 1485331072, 1, 1, '1', '1', '1', NULL, NULL, NULL, NULL),
(121, '1', '1', NULL, '$xpgenrqscimportxitem$c95dc94c3bdfb395f13207062fd7e4993a208f397d4d0790ada5377d2b77f4b9', 1485331342, 1, 1485331342, 1, 1, '1', '1', '1', NULL, NULL, NULL, NULL),
(122, '1', '1', NULL, '$xpgenrqscimportxitem$05b60a7eca726863280ab2f02cf0e0f95ea762dbd503cfcc25fa773bb2a63ed3', 1485331379, 1, 1485331379, 1, 1, '1', '1', '1', NULL, NULL, NULL, NULL),
(123, '1', '1', NULL, '$xpgenrqscimportxitem$041d1f7126a12d62067c1e1cf780568760d67ffcbc2dd7ff9b8af6409876fe42', 1485331523, 1, 1485331523, 1, 1, '1', '1', '1', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rqsctest`
--

CREATE TABLE `rqsctest` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `berta_id` int(11) DEFAULT NULL,
  `title_id` int(11) DEFAULT NULL,
  `titleversion_id` int(11) DEFAULT NULL,
  `titlescenario_id` int(11) DEFAULT NULL,
  `osapi_id` int(11) DEFAULT NULL,
  `configuration_id` int(11) DEFAULT NULL,
  `platform_id` int(11) DEFAULT NULL,
  `rqpriority_id` int(11) DEFAULT NULL,
  `subtype_id` int(11) DEFAULT NULL,
  `rqsctest_id` int(11) DEFAULT NULL,
  `rquser_id` int(11) DEFAULT NULL,
  `is_gta` int(11) DEFAULT NULL,
  `frame_form` int(11) DEFAULT NULL,
  `frame_to` int(11) DEFAULT NULL,
  `stream_id` int(11) DEFAULT NULL,
  `new_title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_version` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_scenario` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_api` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_configuration` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_platform` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `rq_type` int(11) DEFAULT NULL,
  `rqcomment` longtext COLLATE utf8_unicode_ci,
  `rqbody` longtext COLLATE utf8_unicode_ci,
  `berta_scenario` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apitrace_path` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus_id` int(11) DEFAULT NULL,
  `rqtest_id` int(11) DEFAULT NULL,
  `rqdesc` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqactions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rgqueuesend` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rgcsvimport` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqsctest`
--

INSERT INTO `rqsctest` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `berta_id`, `title_id`, `titleversion_id`, `titlescenario_id`, `osapi_id`, `configuration_id`, `platform_id`, `rqpriority_id`, `subtype_id`, `rqsctest_id`, `rquser_id`, `is_gta`, `frame_form`, `frame_to`, `stream_id`, `new_title`, `new_version`, `new_scenario`, `new_api`, `new_configuration`, `new_platform`, `request_id`, `rq_type`, `rqcomment`, `rqbody`, `berta_scenario`, `apitrace_path`, `rqstatus_id`, `rqtest_id`, `rqdesc`, `rqactions`, `rgqueuesend`, `rgcsvimport`) VALUES
(21, '1', '1', NULL, '$rqsctest$c5203c3ed2240d6d3361c49df9f4c7c7d333608f53a47547857bb19cabfcabd7', 1, 1, 1486896066, 8011, NULL, 5, 1, 12, 13, NULL, NULL, NULL, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1399, NULL, NULL, NULL, NULL, NULL, NULL, NULL, ';;', NULL, '0', NULL),
(22, '1', '1', NULL, '$rqsctest$b8b68d52f074f740349cd6bc05eec59b2d6e1c0b581d997eea9ee29187d309c4', 1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(23, '2', '2', NULL, '$rqsctest$0dc2d61427fc76c36b8e226a568b130332ebaa1d9ff12a2c45625600ef924b7d', 1, NULL, 1, NULL, NULL, 5, 1, 12, 13, 15, 187, 13, 50, 38, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(24, 'laaabel', '1', NULL, '$xpgenrqsctestxitem$445fe3421d75762c2dd080494e88a4c80dae1f0e1344349aeed885bbf97b76ad', 1, NULL, 1483743809, 1, NULL, 5, 1, 12, 13, 15, 187, 13, 50, 38, NULL, 8010, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(25, 'ggg1', 'ggg', NULL, '$xpgenrqsctestxitem$bc37528bb2af195a92632ded9002c8d73f1235960a6f37b242f67286f42d1f4b', 1484204218, 1, 1484492750, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, '', '', '', '', '', '', 1395, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(26, 'ggg-2', 'ggg-2', NULL, '$xpgenrqsctestxitem$8fe3ff639af550fb98af744a022cd27f631a18ac94bf5b0ab049f62d3e66610f', 1484204409, 1, 1484204409, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, '', '', '', '', '', '', 1396, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(27, 'a2', NULL, NULL, '$xpgenrqsctestxitem$6d84154edf6c65aa3d34d555c3684716a81b50598ae429b24c55a399dd2f1bf3', 1484492769, 1, 1484492769, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 26, NULL, NULL, NULL, NULL, NULL),
(28, 'aa', NULL, NULL, '$xpgenrqsctestxitem$cc4562e25ad7843b9957710246dbcce949ccfa6eee4249aa5d53b18acd323dff', 1484635506, 1, 1485551314, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 50, 38, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1397, NULL, NULL, NULL, NULL, NULL, 25, 1, NULL, NULL, '1', NULL),
(29, 'ooooon', NULL, NULL, '$xpgenrqsctestxitem$34bd8891a3fb219bd70b7d0aded8a7bace689cce9f347cfe8ecc516277ceed60', 1485691703, 8011, 1486896025, 8011, NULL, NULL, 1, NULL, NULL, 16, 186, 14, 50, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, 1398, NULL, NULL, NULL, NULL, NULL, 25, 1, ';status-1;', NULL, '0', NULL),
(30, 'ala-90', NULL, NULL, '$xpgenrqsctestxitem$b0ce19c7f75cf62e65c702152497d33a978ad9f93fd7d0a04eca9cf812a504fc', 1486896998, 8011, 1486897037, 8011, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1400, NULL, 'ala90-changed', NULL, NULL, NULL, NULL, 1, ';;', NULL, '0', NULL),
(31, 'noowe', NULL, NULL, '$xpgenrqsctestxitem$b77f07b90c97a40e21247e968738a7effd1294b9c34caea0c14f98a5fa60fb32', 1487286886, 8011, 1487286886, 8011, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1401, NULL, NULL, NULL, NULL, NULL, NULL, NULL, ';;', NULL, '0', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rqsctest_completion`
--

CREATE TABLE `rqsctest_completion` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqsctest_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `test_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqactions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rquser_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqsctest_completion`
--

INSERT INTO `rqsctest_completion` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqkey`, `rqvalue`, `rqsctest_id`, `test_id`, `rqstatus`, `rqactions`, `rquser_id`, `rqstatus_id`) VALUES
(120, '1', '1', NULL, '$xpgenrqsctest_completionxitem$7f1354b3bee6131f819d3b1696ed4d2c65dbbb9aca11385e824cfdf7802f7a98', 1485479359, 1, 1485479359, 1, NULL, NULL, NULL, NULL, '1', NULL, NULL, '8009', '25'),
(121, 'aa', 'aa', NULL, NULL, NULL, NULL, 1485551585, 1, NULL, '1', '1', '28', '1', NULL, NULL, '8010', '25'),
(122, '1', '1', NULL, '$rqsctest$c5203c3ed2240d6d3361c49df9f4c7c7d333608f53a47547857bb19cabfcabd7', 1, 1, 1485598385, 1, NULL, NULL, NULL, '21', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rqsctest_test`
--

CREATE TABLE `rqsctest_test` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqsctest_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `test_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqstatus` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqactions` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqsctest_test`
--

INSERT INTO `rqsctest_test` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqkey`, `rqvalue`, `rqsctest_id`, `test_id`, `rqstatus`, `rqactions`) VALUES
(120, '1', '1', NULL, '$xpgenrqsctest_testxitem$58bed3b4a5921c661c40406067671a7cdea67bff8de993f504e5401e6344de02', 1485457782, 1, 1486451235, 8011, 1, '1', '1', '24', '1', '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `rqstatus`
--

CREATE TABLE `rqstatus` (
  `id` int(11) NOT NULL,
  `label` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rqstatus`
--

INSERT INTO `rqstatus` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`) VALUES
(25, 'status-1', 'status-1-slug', NULL, '$xpgenrqstatusxitem$d88e5a7ffd617bc9547ef55c361774dcf619b1879782942c45209e910cdff7ca', 1, 1, 1, 1, 1),
(26, 'status-2', 'status-2-slug', NULL, '$xpgenrqstatusxitem$2a594c656141fbb61a41b86c2d18c4adf30e5c7f64354e43e7b48a137c36f01c', 1, 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `rqsysparam`
--

CREATE TABLE `rqsysparam` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqsysparam`
--

INSERT INTO `rqsysparam` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rqkey`, `rqvalue`) VALUES
(35, 'show_admin', 'show_admin', NULL, '$xpgenrqsysparamxitem$53b2a32fa8ab145759f100dd9c276dc73327f0cb557c909091e55681f7316b96', 1484081254, 1, 1485713476, 8012, 1, 'show_admin', '0'),
(36, 'show_admin_crud', 'show_admin_crud', NULL, '$xpgenrqsysparamxitem$b17346f4c68c431377ce965765e98b9e364f2675e1eb2cc6aa7434e2e8f053bd', 1485694419, 8011, 1487273434, 8011, NULL, 'show_admin_crud', '1'),
(37, 'show_admin_jx', 'show_admin_jx', NULL, '$xpgenrqsysparamxitem$4476ace79c52c57e7c49593152d76ea4781a4f535d32c3287d438be282d94b48', 1485713360, 8012, 1486939645, 8011, NULL, 'show_admin_jx', '1'),
(38, 'show_admin_sc', 'show_admin_sc', NULL, '$xpgenrqsysparamxitem$595a76c9a16175a8530e4acdd38c1d8bd180b9213b381fdf139e137a4c38238d', 1485713504, 8012, 1486409399, 8011, NULL, 'show_admin_sc', '1'),
(39, 'show_oper_streams', 'show_oper_streams', NULL, '$xpgenrqsysparamxitem$45eb1bb4d1b83257c6ef188c35fe4ea3cab0f8630674a840c2530497ad78b126', 1485715657, 8012, 1485715657, 8012, NULL, 'show_oper_streams', '0'),
(40, 'show_oper_scate', 'show_oper_scate', NULL, '$xpgenrqsysparamxitem$3cd36cc888d43f95a5a82cc938d0417784652a04fb2737878e96c0ef56230a2f', 1485715700, 8012, 1485715700, 8012, NULL, 'show_oper_scate', '1'),
(41, 'show_oper_scate_tech', 'show_oper_scate_tech', NULL, '$xpgenrqsysparamxitem$b7c710e9dee0dc56572b49bd77f158a4fa792f4600a494d3cb2466570fbce032', 1485715718, 8012, 1487284430, 8011, NULL, 'show_oper_scate_tech', '1'),
(42, 'show_oper_login', 'show_oper_login', NULL, '$xpgenrqsysparamxitem$4af40dea4f695e08c12adcb7603e004fb35c252d22b355ed9a1765f2656f069c', 1485800833, 1, 1485800833, 1, NULL, 'show_oper_login', '1'),
(43, 'show_oper_requests_all', 'show_oper_requests_all', NULL, '$xpgenrqsysparamxitem$cd1356c020dc85b70994a82414705bb379d196c84e4c61b63ba0bc55703c4c07', 1485800888, 1, 1485800936, 1, NULL, 'show_oper_requests_all', '0'),
(44, 'show_oper_login', 'show_oper_login', NULL, '$xpgenrqsysparamxitem$a90093462ba82cef7c03b2dcbe9248f2313ca76a3011150ef9e036d28459a5ad', 1485800921, 1, 1485800921, 1, NULL, 'show_oper_login', '1'),
(45, 'show_admin_import', 'show_admin_import', NULL, '$xpgenrqsysparamxitem$3298b783c7d8d54ae2c1b2e74ff5ad9b5afa19ac9b7681db48f30524c7bca9ab', 1485802308, 8012, 1485802308, 8012, NULL, 'show_admin_import', '1'),
(46, 'show_admin_import', 'show_admin_import', NULL, '$xpgenrqsysparamxitem$82d0b024d8e8af994b49bed7f275fe7269391b1162a60749ed3b1cce64780e6f', 1485802591, 8012, 1485802591, 8012, NULL, 'show_admin_import', '1'),
(47, 'show_admin_roles', 'show_admin_roles', NULL, '$xpgenrqsysparamxitem$23d5a630c75f8e53ee63a3f7a4edc6a0ca5740f2bb036595ed96b584219948cd', 1485802602, 8012, 1485802602, 8012, NULL, 'show_admin_roles', '1'),
(48, 'show_admin_columns', 'show_admin_columns', NULL, '$xpgenrqsysparamxitem$20da543aeb33ea72beed1837a0bd165968ff5e470fc823317c3358bd651af407', 1485802912, 8012, 1485802912, 8012, NULL, 'show_admin_columns', '1'),
(49, 'show_oper_scate_features', 'show_oper_scate_features', NULL, '$xpgenrqsysparamxitem$49f41ba4aa3e9485c2d932f45295515288c5d90872381c287004fac54ee446b3', 1486890059, 8011, 1486890059, 8011, NULL, 'show_oper_scate_features', '1'),
(50, 'show_priorities', 'show_priorities', NULL, '$xpgenrqsysparamxitem$a23b4358320147a16718b264bd23b839d7cdbdb78606cca5781e15ca230dc6a7', 1487284887, 8011, 1487284887, 8011, NULL, 'show_priorities', '1'),
(51, 'show_main', NULL, NULL, '$xpgenrqsysparamxitem$f91ca936495bbb61e0f3a7d3fb006d6d9bede22797fa8b079f619ace6c93d39b', 1487284906, 8011, 1487284906, 8011, NULL, 'show_main', '1'),
(52, 'show_all', 'show_all', NULL, '$xpgenrqsysparamxitem$6f5b73c8a41d81b5a28ed4896d1fc895a66a471050cf21c0877eee344c18137c', 1487284922, 8011, 1487284922, 8011, NULL, 'show_all', '1'),
(53, 'show_opermain', 'show_opermain', NULL, '$xpgenrqsysparamxitem$de050a591d5d193ca4ce4ba6ee6fe000c0a84d51f7d80675590d15df33ba8367', 1487286696, 8011, 1487286696, 8011, NULL, 'show_opermain', '1'),
(54, 'show_adminmain', 'show_adminmain', NULL, '$xpgenrqsysparamxitem$a1c147a46d4b4643b264153302301694c1c28957896ccc3ff0301644de70fbcc', 1487286778, 8011, 1487286778, 8011, NULL, 'show_adminmain', '1'),
(55, 'show_direct_rq', 'show_direct_rq', NULL, '$xpgenrqsysparamxitem$248a3f0cec9b305145aa3f4248db385c6f5fcb675f7be116956ac6045f763328', 1487287271, 8011, 1487287271, 8011, NULL, 'show_direct_rq', '1');

-- --------------------------------------------------------

--
-- Table structure for table `rqtitle`
--

CREATE TABLE `rqtitle` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `title_id` int(11) DEFAULT NULL,
  `titleversion_id` int(11) DEFAULT NULL,
  `titlescenario_id` int(11) DEFAULT NULL,
  `new_title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_version` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `new_scenario` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rq_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rqtitle`
--

INSERT INTO `rqtitle` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `title_id`, `titleversion_id`, `titlescenario_id`, `new_title`, `new_version`, `new_scenario`, `rq_type`) VALUES
(1, '1', '1', NULL, '$epgenrqtitle$1cb5240d966d087bd4788d9cc2a75db6af2575049054127012c2a8eca93dfb42', 1, 1, 1, 1, 1, 1, 1, 1, '1', '1', '1', 1),
(2, '2', '2', NULL, '$epgenrqtitle$bfba9ace5571d10f5104d5c03244f63625218e50e0dcaf7f36fa1bfd315f3a21', 2, NULL, 1483294916, 1, NULL, 1, 12, 13, NULL, NULL, NULL, NULL),
(3, '4', '4', NULL, '$epgenrqtitle$af5bd56f23495d9624290f22c6fea101fe6b9b67a3200ced013e6958d2b489d0', 4, NULL, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, '11', '11', NULL, '$epgenrqtitle$04f1e9f832f1ecfcffd8ce22a212564d79c37a22f7956179f394153485ff8f41', 1, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rquserrole`
--

CREATE TABLE `rquserrole` (
  `id` int(11) NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `rqorder` int(11) DEFAULT NULL,
  `rquserroletype_id` int(11) DEFAULT NULL,
  `rqtypekey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqkey` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqvalue` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rquser_id` int(11) DEFAULT NULL,
  `rqrole_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `rquserrole`
--

INSERT INTO `rquserrole` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `rqorder`, `rquserroletype_id`, `rqtypekey`, `rqkey`, `rqvalue`, `rquser_id`, `rqrole_id`) VALUES
(1, '1', '1', NULL, '$xpgenrquserrolexitem$f1afd0351c8dc589d3fce204dd473aa21a7699ebaa08551180c24802d20bf150', 1485479746, 1, 1485479746, 1, NULL, NULL, NULL, NULL, NULL, 8009, 1),
(2, '1', '1', NULL, '$xpgenrquserrolexitem$6e311b1c3f7874860e7baa5633619b6da18abec74dbf92315b51dafbd5e0e612', 1486808281, 8011, 1486853874, 8011, NULL, NULL, NULL, '1', '1', 8011, 2);

-- --------------------------------------------------------

--
-- Table structure for table `scurve`
--

CREATE TABLE `scurve` (
  `id` int(11) NOT NULL,
  `label` varchar(100) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `start_date` int(11) NOT NULL,
  `end_date` int(11) NOT NULL,
  `period_symbol` varchar(20) NOT NULL,
  `submitted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `scurve_workloads`
--

CREATE TABLE `scurve_workloads` (
  `scurve_id` int(11) NOT NULL,
  `workload_id` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `isstart` tinyint(1) NOT NULL,
  `isfinish` tinyint(1) NOT NULL,
  `color` varchar(20) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`id`, `name`, `symbol`, `isstart`, `isfinish`, `color`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `revision`) VALUES
(29, 'status-2', 'status-2-symbol', 1, 1, '1', '$xpgenstatusxitem$f32cb6528b2296a39f8125e7d45eaa3f7d7c11ed7631f2cee444508c2bf0492b', 1483294208, 1, 1483294237, 1, NULL),
(30, 'ststus-new', '1', 1, 1, '1', '$xpgenstatusxitem$84e8fd69647a960ab712d40064e079bfee87f8f9431c1fad0ae05148a48c8a5b', 1483294264, 1, 1483294264, 1, NULL),
(31, 'new', 'new', 1, 1, '1', '$xpgenstatusxitem$1fc97ffbec610b3a9f1e08b1c054137aaea2c1849190d80fea6959f534c9f4da', 1484203257, 1, 1485550884, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `streams`
--

CREATE TABLE `streams` (
  `id` int(11) NOT NULL,
  `label` int(11) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `scenario` int(11) DEFAULT NULL,
  `configuration` int(11) DEFAULT NULL,
  `api` int(11) DEFAULT NULL,
  `submitted` int(11) NOT NULL,
  `platform` int(11) DEFAULT NULL,
  `is_frame` int(11) NOT NULL,
  `stream_binary_location` text CHARACTER SET latin1,
  `stream_weights_location` text CHARACTER SET latin1,
  `parent` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `streams`
--

INSERT INTO `streams` (`id`, `label`, `version`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `revision`, `scenario`, `configuration`, `api`, `submitted`, `platform`, `is_frame`, `stream_binary_location`, `stream_weights_location`, `parent`) VALUES
(1, NULL, NULL, '$xpgenstreamsxitem$a28f87dc02507afc220f0a991e8e39263d1e6a40d45f3cd0dd41b1c22fbafbda', 1484513931, 1, 1484513931, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL),
(2, 1, NULL, '$xpgenstreamsxitem$bab1be5af6679c7de19851f0f5bb5b163b1bba1f243dfc646ec0d9c95d296fc5', 1484513977, 1, 1484513977, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, '1', NULL, NULL),
(3, NULL, NULL, '$xpgenstreamsxitem$edbe703afdb5c320fc7bd6932f51d7709ed09f2a1b06ea70b2b2efc0ff51591a', 1484514912, 1, 1484514912, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, '1', NULL, NULL),
(4, 1, NULL, '$xpgenstreamsxitem$883361978bd049457af9efc8a357aaf74890eadf48100f02e58b8df92f64f7c6', 1484515382, 1, 1484515382, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, '1', NULL, NULL),
(5, 1, NULL, '$xpgenstreamsxitem$4d98f48a76ae8230448efc60e1e8fc01934dc97cbd71400586ace9fc9e783f7b', 1484515514, 1, 1484515514, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, '1', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `stream_frames`
--

CREATE TABLE `stream_frames` (
  `id` int(11) NOT NULL,
  `label` varchar(255) DEFAULT NULL,
  `description` text,
  `single` int(11) NOT NULL,
  `binary_url` text NOT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `stream` int(11) DEFAULT NULL,
  `origin_url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `stream_frames_range`
--

CREATE TABLE `stream_frames_range` (
  `id` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `stream` int(11) DEFAULT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `start` int(11) NOT NULL,
  `end` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `id` int(11) NOT NULL,
  `label` varchar(255) DEFAULT NULL,
  `uid` int(11) NOT NULL,
  `origin_url` text NOT NULL,
  `type` int(11) DEFAULT NULL,
  `request` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `request_type` int(11) DEFAULT NULL,
  `body` varchar(4000) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `rqbody` varchar(4000) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `subtype`
--

CREATE TABLE `subtype` (
  `id` int(11) NOT NULL,
  `label` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subtype`
--

INSERT INTO `subtype` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`) VALUES
(38, 'subtype-1', 'subtype-1-slug', NULL, '$xpgensubtypexitem$ea50303dd71b5ad5681dcc6f75a833b29ac44b26be84b484cf2a3ae44e291602', 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tests`
--

CREATE TABLE `tests` (
  `id` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `stream_id` int(11) DEFAULT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) NOT NULL,
  `changed_at` int(11) NOT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `submitted` int(11) NOT NULL,
  `berta` int(11) DEFAULT NULL,
  `berta_scenario` text COLLATE utf8_unicode_ci,
  `is_gta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tests`
--

INSERT INTO `tests` (`id`, `created_by`, `revision`, `stream_id`, `changed_by`, `label`, `created_at`, `changed_at`, `hash`, `submitted`, `berta`, `berta_scenario`, `is_gta`) VALUES
(1, 1, NULL, 4, 1, 'ala', 1484635445, 1484635446, '$xpgentestsxitem$2662dfcdad2706b08f2b75123275ba1833fb3b9ceca58eb3e95c7ed0f1307838', 1, 6, '1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `title`
--

CREATE TABLE `title` (
  `id` int(11) NOT NULL,
  `isgame` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `binary_url` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `title`
--

INSERT INTO `title` (`id`, `isgame`, `name`, `created_at`, `created_by`, `changed_at`, `changed_by`, `hash`, `revision`, `binary_url`) VALUES
(1, 1, '1', 1, 1, 1, 1, '1', 1, '1'),
(2144, 1, 'title-2', 1483869339, 1, 1483869339, 1, '$xpgentitlexitem$f585cf8afa1e22beb38b7fc07deb0dea414339238ab6034444ed54a5a6483668', NULL, 'aa'),
(2145, 1, '1', 1483907101, 1, 1483907101, 1, '$xpgentitlexitem$cd89ce347d238a0b90dfed455ab570c1dbd9ef90ec79d4841520b3ce7d20597d', NULL, '1'),
(2146, 1, 'name1', 1484631404, 1, 1484631404, 1, '$xpgentitlexitem$108579cb1e445c2953de5f74991a6828633225b04eaca1dda3d4eb5ffe2c3a0e', NULL, '1');

-- --------------------------------------------------------

--
-- Table structure for table `titlealias`
--

CREATE TABLE `titlealias` (
  `id` int(11) NOT NULL,
  `title_id` int(11) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `titlealias`
--

INSERT INTO `titlealias` (`id`, `title_id`, `name`, `created_at`, `created_by`, `changed_at`, `changed_by`, `hash`, `revision`) VALUES
(3540, 1, 'name-1', 1, 1, 1, 1, '$xpgentitlealiasxitem$3a12717f98bbaaf1df5acd9142c9e24d645a53922380bf8decb5639177a1436d', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `title_scenario`
--

CREATE TABLE `title_scenario` (
  `id` int(11) NOT NULL,
  `label` varchar(255) NOT NULL,
  `title` int(11) DEFAULT NULL,
  `title_version` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `title_scenario`
--

INSERT INTO `title_scenario` (`id`, `label`, `title`, `title_version`, `hash`, `revision`, `created_at`, `created_by`, `changed_at`, `changed_by`) VALUES
(13, 'title-scen-1', NULL, NULL, '$xpgentitle_scenarioxitem$b7871c6557bf4df19db171c744cf8cdc985dee7877adbb15503ac49a6e8b6522', NULL, 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `title_version`
--

CREATE TABLE `title_version` (
  `id` int(11) NOT NULL,
  `label` varchar(50) NOT NULL,
  `title` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `ptf_location` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `title_version`
--

INSERT INTO `title_version` (`id`, `label`, `title`, `hash`, `revision`, `created_at`, `created_by`, `changed_at`, `changed_by`, `ptf_location`) VALUES
(12, 'titlever-1', NULL, '$xpgentitle_versionxitem$be5c89d88f13c90f99d5ed4bd6d5c6865f8f5a4d618d7fef7508be886fd1aff0', NULL, 1, 1, 1, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `type`
--

CREATE TABLE `type` (
  `id` int(11) NOT NULL,
  `label` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `revision` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `type`
--

INSERT INTO `type` (`id`, `label`, `slug`, `revision`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`) VALUES
(36, 'label-1', 'slug-1', NULL, '$xpgentypexitem$3c6cfc8294677fbe622b1c742432ffa99e54e96de55f84cc313b5fc7ae5b744b', 1, 1, 1, 1),
(37, 'type-new', 'type-new', NULL, '$xpgentypexitem$5a871ac1405fbbe60c3f9caf8e89fa4ea6e8a48ac535b5fc919b8497b44b67c5', 1483603977, 1, 1483603977, 1),
(38, 'lb-4', 's-4', NULL, '$xpgentypexitem$f4f59a3e2640387dc1331e0b439c3747edf38133a71a8d6e66b28eab7d47e22d', 1483868026, 1, 1483868026, 1),
(39, 'test', 'test', NULL, '$xpgentypexitem$7866b59ae9ddedc5570c498165353502a3c592c08f2f5d768c5825624d281b71', 1484202096, 1, 1484202096, 1),
(40, 'substream', 'substream', NULL, '$xpgentypexitem$35af815d4a5a51600096e57a2d9529a064c61f24a9e62cae5126d83334fafbb0', 1484630951, 1, 1484630951, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `wwid` int(11) NOT NULL,
  `created_at` int(11) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `wwid`, `created_at`, `display_name`) VALUES
(1, 'user-1', 'user-1', 1, 1, 'user-1'),
(8009, 'user-2', 'user-email', 11, 1, 'user-display'),
(8010, 'user-2', 'user-email', 11, 1, 'user-display'),
(8011, 'jacek.tracz', 'email', 2134, 1485691127, 'jacek tracz'),
(8012, 'jacek.tracz2', 'email', 2136, 1485713155, 'jacek-tracz-2');

-- --------------------------------------------------------

--
-- Table structure for table `workload`
--

CREATE TABLE `workload` (
  `id` int(11) NOT NULL,
  `title` int(11) DEFAULT NULL,
  `api` int(11) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `created_at` int(11) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `changed_at` int(11) NOT NULL,
  `changed_by` int(11) DEFAULT NULL,
  `revision` int(11) DEFAULT NULL,
  `platform` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `workload`
--

INSERT INTO `workload` (`id`, `title`, `api`, `hash`, `created_at`, `created_by`, `changed_at`, `changed_by`, `revision`, `platform`) VALUES
(121, 1, 16, '$xpgenworkloadxitem$b66c8eaef305542696c93a3dbb0d9847427855d2a8515a568bc576de56639ac1', 1483489237, 1, 1483489237, 1, 7068, 13),
(122, 1, 16, '$xpgenworkloadxitem$9ad51a13b7f6b81366f17962bb7a8c55825519af6b913459c0d00b77e7ce34eb', 1483869224, 1, 1483869224, 1, NULL, 13),
(123, 2144, 18, '$xpgenworkloadxitem$f9c7343a5efd1bb3c34df971eb2ab3bcdd3a11c3ae8e503e63454846fee4414e', 1483869375, 1, 1483869375, 1, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bertas`
--
ALTER TABLE `bertas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `berta_created_by` (`created_by`),
  ADD KEY `berta_changed_by` (`changed_by`),
  ADD KEY `berta_revision` (`revision`);

--
-- Indexes for table `configurations`
--
ALTER TABLE `configurations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `configuration_changed_by` (`changed_by`),
  ADD KEY `configuration_created_by` (`created_by`),
  ADD KEY `configuration_revision` (`revision`),
  ADD KEY `configuration_hash` (`hash`);

--
-- Indexes for table `configuration_fields`
--
ALTER TABLE `configuration_fields`
  ADD PRIMARY KEY (`id`),
  ADD KEY `conffield_created_by` (`created_by`),
  ADD KEY `conffield_changed_by` (`changed_by`),
  ADD KEY `conffield_revision` (`revision`),
  ADD KEY `conffield_configuration` (`configuration`);

--
-- Indexes for table `doctrine_migration_versions`
--
ALTER TABLE `doctrine_migration_versions`
  ADD PRIMARY KEY (`version`);

--
-- Indexes for table `operation_system`
--
ALTER TABLE `operation_system`
  ADD PRIMARY KEY (`id`),
  ADD KEY `os_created_by` (`created_by`),
  ADD KEY `os_family` (`family_id`),
  ADD KEY `os_revision` (`revision`),
  ADD KEY `os_changed_by` (`changed_by`),
  ADD KEY `os_hash` (`hash`);

--
-- Indexes for table `osfamily`
--
ALTER TABLE `osfamily`
  ADD PRIMARY KEY (`id`),
  ADD KEY `osfamily_revision` (`revision`),
  ADD KEY `osfamily_created_by` (`created_by`),
  ADD KEY `osfamily_changed_by` (`changed_by`);

--
-- Indexes for table `os_api`
--
ALTER TABLE `os_api`
  ADD PRIMARY KEY (`id`),
  ADD KEY `apis_changed_by` (`changed_by`),
  ADD KEY `apis_created_by` (`created_by`),
  ADD KEY `apis_osfamily` (`osfamily`),
  ADD KEY `apis_revision` (`revision`),
  ADD KEY `os_api_hash` (`hash`);

--
-- Indexes for table `platforms`
--
ALTER TABLE `platforms`
  ADD PRIMARY KEY (`id`),
  ADD KEY `platform_created_by` (`created_by`),
  ADD KEY `platform_changed_by` (`changed_by`),
  ADD KEY `platform_revision` (`revision`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `projects_changed_by` (`changed_by`),
  ADD KEY `projects_created_by` (`created_by`),
  ADD KEY `projects_revision` (`revision`);

--
-- Indexes for table `projects_streams`
--
ALTER TABLE `projects_streams`
  ADD PRIMARY KEY (`project`,`stream`),
  ADD KEY `IDX_223C61EB2FB3D0EE` (`project`),
  ADD KEY `IDX_223C61EBF0E9BE1C` (`stream`);

--
-- Indexes for table `projects_workloads`
--
ALTER TABLE `projects_workloads`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_577A32A1203AA7B` (`workload`),
  ADD KEY `FK_577A32A2FB3D0EE` (`project`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `request_assigned_to` (`assignedTo`),
  ADD KEY `request_changed_by` (`changed_by`),
  ADD KEY `request_created_by` (`created_by`),
  ADD KEY `request_revision` (`revision`),
  ADD KEY `IDX_3B978F9F7B00651C` (`status`),
  ADD KEY `IDX_3B978F9F8CDE5729` (`type`);

--
-- Indexes for table `rqdefcolumn`
--
ALTER TABLE `rqdefcolumn`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqdefview`
--
ALTER TABLE `rqdefview`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqpriority`
--
ALTER TABLE `rqpriority`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rqpriority_created_by` (`created_by`),
  ADD KEY `rqpriority_changed_by` (`changed_by`),
  ADD KEY `rqpriority_revision` (`revision`);

--
-- Indexes for table `rqrole`
--
ALTER TABLE `rqrole`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rqrole_created_by` (`created_by`),
  ADD KEY `rqrole_changed_by` (`changed_by`),
  ADD KEY `rqrole_revision` (`revision`);

--
-- Indexes for table `rqrole_status`
--
ALTER TABLE `rqrole_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqscimp`
--
ALTER TABLE `rqscimp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqscimport`
--
ALTER TABLE `rqscimport`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqsctest`
--
ALTER TABLE `rqsctest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rqsctest_created_by` (`created_by`),
  ADD KEY `rqsctest_changed_by` (`changed_by`),
  ADD KEY `rqsctest_revision` (`revision`);

--
-- Indexes for table `rqsctest_completion`
--
ALTER TABLE `rqsctest_completion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqsctest_test`
--
ALTER TABLE `rqsctest_test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rqstatus`
--
ALTER TABLE `rqstatus`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rqstatus_created_by` (`created_by`),
  ADD KEY `rqstatus_changed_by` (`changed_by`),
  ADD KEY `rqstatus_revision` (`revision`);

--
-- Indexes for table `rqsysparam`
--
ALTER TABLE `rqsysparam`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rqsysparam_created_by` (`created_by`),
  ADD KEY `rqsysparam_changed_by` (`changed_by`),
  ADD KEY `rqsysparam_revision` (`revision`);

--
-- Indexes for table `rqtitle`
--
ALTER TABLE `rqtitle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rqtitle_created_by` (`created_by`),
  ADD KEY `rqtitle_changed_by` (`changed_by`),
  ADD KEY `rqtitle_revision` (`revision`);

--
-- Indexes for table `rquserrole`
--
ALTER TABLE `rquserrole`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rquserrole_created_by` (`created_by`),
  ADD KEY `rquserrole_changed_by` (`changed_by`),
  ADD KEY `rquserrole_revision` (`revision`);

--
-- Indexes for table `scurve`
--
ALTER TABLE `scurve`
  ADD PRIMARY KEY (`id`),
  ADD KEY `scurve_revision` (`revision`),
  ADD KEY `scurve_created_by` (`created_by`),
  ADD KEY `scurve_changed_by` (`changed_by`),
  ADD KEY `scurve_period` (`period_symbol`),
  ADD KEY `scurve_start_date` (`start_date`),
  ADD KEY `scurve_end_date` (`end_date`);

--
-- Indexes for table `scurve_workloads`
--
ALTER TABLE `scurve_workloads`
  ADD PRIMARY KEY (`scurve_id`,`workload_id`),
  ADD KEY `IDX_651BC4D36A9311DC` (`scurve_id`),
  ADD KEY `IDX_651BC4D3F304474A` (`workload_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`),
  ADD KEY `status_changed_by` (`changed_by`),
  ADD KEY `status_created_by` (`created_by`),
  ADD KEY `status_revision` (`revision`);

--
-- Indexes for table `streams`
--
ALTER TABLE `streams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `benchmark_version` (`version`),
  ADD KEY `benchmark_hash` (`hash`),
  ADD KEY `benchmark_changed_by` (`changed_by`),
  ADD KEY `benchmark_configuration` (`configuration`),
  ADD KEY `benchmark_created_by` (`created_by`),
  ADD KEY `benchmark_label` (`label`),
  ADD KEY `benchmark_revision` (`revision`),
  ADD KEY `benchmark_api` (`api`),
  ADD KEY `stream_platform` (`platform`),
  ADD KEY `stream_scenario` (`scenario`),
  ADD KEY `IDX_FFF7AFA3D8E604F` (`parent`);

--
-- Indexes for table `stream_frames`
--
ALTER TABLE `stream_frames`
  ADD PRIMARY KEY (`id`),
  ADD KEY `streamframe_changed_by` (`changed_by`),
  ADD KEY `streamframe_stream` (`stream`);

--
-- Indexes for table `stream_frames_range`
--
ALTER TABLE `stream_frames_range`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sfr_created_by` (`created_by`),
  ADD KEY `sfx_changed_by` (`changed_by`),
  ADD KEY `sfx_revision` (`revision`),
  ADD KEY `sfx_stream` (`stream`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`id`),
  ADD KEY `subject_request` (`request`),
  ADD KEY `subject_type` (`type`),
  ADD KEY `subject_revision` (`revision`),
  ADD KEY `subject_created_by` (`created_by`),
  ADD KEY `IDX_FBCE3E7AF37970D3` (`request_type`);

--
-- Indexes for table `subtype`
--
ALTER TABLE `subtype`
  ADD PRIMARY KEY (`id`),
  ADD KEY `subtype_created_by` (`created_by`),
  ADD KEY `subtype_changed_by` (`changed_by`),
  ADD KEY `subtype_revision` (`revision`);

--
-- Indexes for table `tests`
--
ALTER TABLE `tests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `test_created_by` (`created_by`),
  ADD KEY `test_revision` (`revision`),
  ADD KEY `test_changed_by` (`changed_by`),
  ADD KEY `test_hash` (`hash`),
  ADD KEY `test_stream` (`stream_id`),
  ADD KEY `IDX_1260FC5EFBB8503` (`berta`);

--
-- Indexes for table `title`
--
ALTER TABLE `title`
  ADD PRIMARY KEY (`id`),
  ADD KEY `title_changed_by` (`changed_by`),
  ADD KEY `title_created_by` (`created_by`),
  ADD KEY `title_revision` (`revision`),
  ADD KEY `title_hash` (`hash`);

--
-- Indexes for table `titlealias`
--
ALTER TABLE `titlealias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `titlealias_created_by` (`created_by`),
  ADD KEY `titlealias_revision` (`revision`),
  ADD KEY `titlealias_title` (`title_id`),
  ADD KEY `titlealiast_changed_by` (`changed_by`),
  ADD KEY `titlealias_hash` (`hash`);

--
-- Indexes for table `title_scenario`
--
ALTER TABLE `title_scenario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `title_scenario_title` (`title`),
  ADD KEY `title_scenarion_changed_by` (`changed_by`),
  ADD KEY `title_scenarion_created_by` (`created_by`),
  ADD KEY `title_scenarion_revision` (`revision`),
  ADD KEY `title_scenarion_version` (`title_version`);

--
-- Indexes for table `title_version`
--
ALTER TABLE `title_version`
  ADD PRIMARY KEY (`id`),
  ADD KEY `title_version_title` (`title`),
  ADD KEY `title_version_revision` (`revision`),
  ADD KEY `title_version_created_by` (`created_by`),
  ADD KEY `title_version_changed_by` (`changed_by`);

--
-- Indexes for table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`id`),
  ADD KEY `type_created_by` (`created_by`),
  ADD KEY `type_changed_by` (`changed_by`),
  ADD KEY `type_revision` (`revision`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_wwid` (`wwid`),
  ADD KEY `user_username` (`username`);

--
-- Indexes for table `workload`
--
ALTER TABLE `workload`
  ADD PRIMARY KEY (`id`),
  ADD KEY `workload_revision` (`revision`),
  ADD KEY `workload_created_by` (`created_by`),
  ADD KEY `workload_changed_by` (`changed_by`),
  ADD KEY `workload_title` (`title`),
  ADD KEY `workload_api` (`api`),
  ADD KEY `workload_platform` (`platform`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bertas`
--
ALTER TABLE `bertas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `configurations`
--
ALTER TABLE `configurations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=189;
--
-- AUTO_INCREMENT for table `configuration_fields`
--
ALTER TABLE `configuration_fields`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `operation_system`
--
ALTER TABLE `operation_system`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `osfamily`
--
ALTER TABLE `osfamily`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `os_api`
--
ALTER TABLE `os_api`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `platforms`
--
ALTER TABLE `platforms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `projects_workloads`
--
ALTER TABLE `projects_workloads`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;
--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1402;
--
-- AUTO_INCREMENT for table `rqdefcolumn`
--
ALTER TABLE `rqdefcolumn`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
--
-- AUTO_INCREMENT for table `rqdefview`
--
ALTER TABLE `rqdefview`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
--
-- AUTO_INCREMENT for table `rqpriority`
--
ALTER TABLE `rqpriority`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
--
-- AUTO_INCREMENT for table `rqrole`
--
ALTER TABLE `rqrole`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `rqrole_status`
--
ALTER TABLE `rqrole_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
--
-- AUTO_INCREMENT for table `rqscimp`
--
ALTER TABLE `rqscimp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;
--
-- AUTO_INCREMENT for table `rqscimport`
--
ALTER TABLE `rqscimport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;
--
-- AUTO_INCREMENT for table `rqsctest`
--
ALTER TABLE `rqsctest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `rqsctest_completion`
--
ALTER TABLE `rqsctest_completion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;
--
-- AUTO_INCREMENT for table `rqsctest_test`
--
ALTER TABLE `rqsctest_test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;
--
-- AUTO_INCREMENT for table `rqstatus`
--
ALTER TABLE `rqstatus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `rqsysparam`
--
ALTER TABLE `rqsysparam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;
--
-- AUTO_INCREMENT for table `rqtitle`
--
ALTER TABLE `rqtitle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `rquserrole`
--
ALTER TABLE `rquserrole`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `scurve`
--
ALTER TABLE `scurve`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `streams`
--
ALTER TABLE `streams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `stream_frames`
--
ALTER TABLE `stream_frames`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `stream_frames_range`
--
ALTER TABLE `stream_frames_range`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `subtype`
--
ALTER TABLE `subtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
--
-- AUTO_INCREMENT for table `tests`
--
ALTER TABLE `tests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `title`
--
ALTER TABLE `title`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147;
--
-- AUTO_INCREMENT for table `titlealias`
--
ALTER TABLE `titlealias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3541;
--
-- AUTO_INCREMENT for table `title_scenario`
--
ALTER TABLE `title_scenario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `title_version`
--
ALTER TABLE `title_version`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `type`
--
ALTER TABLE `type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8013;
--
-- AUTO_INCREMENT for table `workload`
--
ALTER TABLE `workload`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `bertas`
--
ALTER TABLE `bertas`
  ADD CONSTRAINT `FK_8208253410BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_820825346D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_82082534DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `configurations`
--
ALTER TABLE `configurations`
  ADD CONSTRAINT `FK_31C6AD910BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_31C6AD96D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_31C6AD9DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `configuration_fields`
--
ALTER TABLE `configuration_fields`
  ADD CONSTRAINT `FK_88C2C41510BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_88C2C4156D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_88C2C415A5E2A5D7` FOREIGN KEY (`configuration`) REFERENCES `configurations` (`id`),
  ADD CONSTRAINT `FK_88C2C415DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `operation_system`
--
ALTER TABLE `operation_system`
  ADD CONSTRAINT `FK_B4CDA8E910BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_B4CDA8E96D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_B4CDA8E9C35E566A` FOREIGN KEY (`family_id`) REFERENCES `osfamily` (`id`),
  ADD CONSTRAINT `FK_B4CDA8E9DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `osfamily`
--
ALTER TABLE `osfamily`
  ADD CONSTRAINT `FK_A54D273010BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_A54D27306D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_A54D2730DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `os_api`
--
ALTER TABLE `os_api`
  ADD CONSTRAINT `FK_373898DA10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_373898DA6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_373898DAA54D2730` FOREIGN KEY (`osfamily`) REFERENCES `osfamily` (`id`),
  ADD CONSTRAINT `FK_373898DADE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `platforms`
--
ALTER TABLE `platforms`
  ADD CONSTRAINT `FK_178186E310BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_178186E36D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_178186E3DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `FK_5C93B3A410BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_5C93B3A46D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_5C93B3A4DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `projects_streams`
--
ALTER TABLE `projects_streams`
  ADD CONSTRAINT `FK_223C61EB2FB3D0EE` FOREIGN KEY (`project`) REFERENCES `projects` (`id`),
  ADD CONSTRAINT `FK_223C61EBF0E9BE1C` FOREIGN KEY (`stream`) REFERENCES `streams` (`id`);

--
-- Constraints for table `projects_workloads`
--
ALTER TABLE `projects_workloads`
  ADD CONSTRAINT `FK_577A32A1203AA7B` FOREIGN KEY (`workload`) REFERENCES `workload` (`id`),
  ADD CONSTRAINT `FK_577A32A2FB3D0EE` FOREIGN KEY (`project`) REFERENCES `projects` (`id`);

--
-- Constraints for table `request`
--
ALTER TABLE `request`
  ADD CONSTRAINT `FK_3B978F9F10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_3B978F9F5B7F11F7` FOREIGN KEY (`assignedTo`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_3B978F9F6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_3B978F9F7B00651C` FOREIGN KEY (`status`) REFERENCES `status` (`id`),
  ADD CONSTRAINT `FK_3B978F9F8CDE5729` FOREIGN KEY (`type`) REFERENCES `type` (`id`),
  ADD CONSTRAINT `FK_3B978F9FDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `scurve`
--
ALTER TABLE `scurve`
  ADD CONSTRAINT `FK_ADCF746610BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_ADCF74666D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_ADCF7466DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `scurve_workloads`
--
ALTER TABLE `scurve_workloads`
  ADD CONSTRAINT `FK_651BC4D36A9311DC` FOREIGN KEY (`scurve_id`) REFERENCES `scurve` (`id`),
  ADD CONSTRAINT `FK_651BC4D3F304474A` FOREIGN KEY (`workload_id`) REFERENCES `workload` (`id`);

--
-- Constraints for table `status`
--
ALTER TABLE `status`
  ADD CONSTRAINT `FK_7B00651C10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_7B00651C6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_7B00651CDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `streams`
--
ALTER TABLE `streams`
  ADD CONSTRAINT `FK_FFF7AFA10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_FFF7AFA3952D0CB` FOREIGN KEY (`platform`) REFERENCES `platforms` (`id`),
  ADD CONSTRAINT `FK_FFF7AFA3D8E604F` FOREIGN KEY (`parent`) REFERENCES `streams` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `FK_FFF7AFA3E45C8D8` FOREIGN KEY (`scenario`) REFERENCES `title_scenario` (`id`),
  ADD CONSTRAINT `FK_FFF7AFA6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_FFF7AFAA5E2A5D7` FOREIGN KEY (`configuration`) REFERENCES `configurations` (`id`),
  ADD CONSTRAINT `FK_FFF7AFAAD05D80F` FOREIGN KEY (`api`) REFERENCES `os_api` (`id`),
  ADD CONSTRAINT `FK_FFF7AFABF1CD3C3` FOREIGN KEY (`version`) REFERENCES `title_version` (`id`),
  ADD CONSTRAINT `FK_FFF7AFADE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_FFF7AFAEA750E8` FOREIGN KEY (`label`) REFERENCES `title` (`id`);

--
-- Constraints for table `stream_frames`
--
ALTER TABLE `stream_frames`
  ADD CONSTRAINT `FK_2441590F10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_2441590FF0E9BE1C` FOREIGN KEY (`stream`) REFERENCES `streams` (`id`);

--
-- Constraints for table `stream_frames_range`
--
ALTER TABLE `stream_frames_range`
  ADD CONSTRAINT `FK_C10678DE10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_C10678DE6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_C10678DEDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_C10678DEF0E9BE1C` FOREIGN KEY (`stream`) REFERENCES `streams` (`id`);

--
-- Constraints for table `subject`
--
ALTER TABLE `subject`
  ADD CONSTRAINT `FKREQUESTTYPE` FOREIGN KEY (`request_type`) REFERENCES `type` (`id`),
  ADD CONSTRAINT `FK_FBCE3E7A3B978F9F` FOREIGN KEY (`request`) REFERENCES `request` (`id`),
  ADD CONSTRAINT `FK_FBCE3E7A6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_FBCE3E7A8CDE5729` FOREIGN KEY (`type`) REFERENCES `type` (`id`),
  ADD CONSTRAINT `FK_FBCE3E7ADE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `tests`
--
ALTER TABLE `tests`
  ADD CONSTRAINT `FK_1260FC5EFBB8503` FOREIGN KEY (`berta`) REFERENCES `bertas` (`id`),
  ADD CONSTRAINT `FK_D87F7E0C10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_D87F7E0C6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_D87F7E0CD0ED463E` FOREIGN KEY (`stream_id`) REFERENCES `streams` (`id`),
  ADD CONSTRAINT `FK_D87F7E0CDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `title`
--
ALTER TABLE `title`
  ADD CONSTRAINT `FK_2B36786B10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_2B36786B6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_2B36786BDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `titlealias`
--
ALTER TABLE `titlealias`
  ADD CONSTRAINT `FK_F793C1F010BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_F793C1F06D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_F793C1F0A9F87BD` FOREIGN KEY (`title_id`) REFERENCES `title` (`id`),
  ADD CONSTRAINT `FK_F793C1F0DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `title_scenario`
--
ALTER TABLE `title_scenario`
  ADD CONSTRAINT `FK_17DE7D7910BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_17DE7D792B36786B` FOREIGN KEY (`title`) REFERENCES `title` (`id`),
  ADD CONSTRAINT `FK_17DE7D796D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_17DE7D79DE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_17DE7D79FD60EABA` FOREIGN KEY (`title_version`) REFERENCES `title_version` (`id`);

--
-- Constraints for table `title_version`
--
ALTER TABLE `title_version`
  ADD CONSTRAINT `FK_FD60EABA10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_FD60EABA2B36786B` FOREIGN KEY (`title`) REFERENCES `title` (`id`),
  ADD CONSTRAINT `FK_FD60EABA6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_FD60EABADE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `workload`
--
ALTER TABLE `workload`
  ADD CONSTRAINT `FK_1203AA7B10BC6D9F` FOREIGN KEY (`changed_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `FK_1203AA7B2B36786B` FOREIGN KEY (`title`) REFERENCES `title` (`id`),
  ADD CONSTRAINT `FK_1203AA7B3952D0CB` FOREIGN KEY (`platform`) REFERENCES `platforms` (`id`),
  ADD CONSTRAINT `FK_1203AA7B6D6315CC` FOREIGN KEY (`revision`) REFERENCES `revision` (`id`),
  ADD CONSTRAINT `FK_1203AA7BAD05D80F` FOREIGN KEY (`api`) REFERENCES `os_api` (`id`),
  ADD CONSTRAINT `FK_1203AA7BDE12AB56` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
