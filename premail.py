from premailer import transform
print(transform("""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Zen Flat Progress Email</title>
  <style type="text/css" media="screen">

    /* Force Hotmail to display emails at full width */
    .ExternalClass {
      display: block !important;
      width: 100%;
    }

    /* Force Hotmail to display normal line spacing */
    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div {
      line-height: 100%;
    }

    body,
    p,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      margin: 0;
      padding: 0;
    }

    body,
    p,
    td {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 15px;
      color: #333333;
    }

    h1 {
      font-size: 24px;
      font-weight: normal;
      line-height: 24px;
    }

    body,
    p {
      margin-bottom: 0;
      -webkit-text-size-adjust: none;
      -ms-text-size-adjust: none;
    }

    img {
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }

    a img {
      border: none;
    }

    .background {
      background-color: #333333;
    }

    table.background {
      margin: 0;
      padding: 0;
      width: 100% !important;
    }

    .block-img {
      display: block;
      line-height: 0;
    }

    a,
    a:link {
      color: #2A5DB0;
      text-decoration: underline;
    }

    table td {
      border-collapse: collapse;
    }

    td {
      vertical-align: top;
      text-align: left;
    }

    .wrap {
      max-width: 600px;
      min-width: 240px;
      margin: 0 auto;
    }

    .wrap-cell {
      padding-top: 30px;
      padding-bottom: 30px;
    }

    .header-cell,
    .body-cell,
    .footer-cell {
      padding-left: 20px;
      padding-right: 20px;
    }

    .header-cell {
      background-color: #eeeeee;
      font-size: 24px;
      color: #ffffff;
    }

    .body-cell {
      background-color: #ffffff;
      padding-top: 30px;
      padding-bottom: 34px;
    }

    .progress .progress-marker {
      width: 24px;
    }

    .progress .progress-line-pad,
    .progress .progress-line {
      width: 8px;
    }

    .progress.progress-completed .progress-line {
      background-color: #8cc57f;
    }

    .progress.progress-active .progress-line {
      background-color: #cdcdcd;
    }

    .progress .progress-title,
    .progress .progress-text {
      padding-left: 12px;
    }

    .progress.progress-completed .progress-title {
      color: #8cc57f;
    }

    .progress.progress-pending .progress-title {
      color: #b2b2b2;
    }

    .progress .progress-text {
      padding-bottom: 20px;
    }

    .footer-cell {
      background-color: #eeeeee;
      text-align: center;
      font-size: 13px;
      padding-top: 20px;
      padding-bottom: 20px;
    }

    .force-full-width {
      width: 100% !important;
    }

    .headlines{
      font-size: 17px;
    }

  </style>
  <style type="text/css" media="only screen and (max-width: 600px)">
    @media only screen and (max-width: 600px) {
      body[class*="background"],
      table[class*="background"],
      td[class*="background"] {
        background: #eeeeee !important;
      }

      table[class="wrap"] { width: 100% !important; }
      td[class="wrap-cell"] { padding-top: 0 !important; padding-bottom: 0 !important; }
    }
  </style>
</head>

<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" class="background">
  <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" class="background">
    <tr>
      <td align="center" valign="top" class="background" width="100%">
        <center>
          <table cellpadding="0" cellspacing="0" width="600" class="wrap">
            <tr>
              <td valign="top" class="wrap-cell">
                <table cellpadding="0" cellspacing="0" class="force-full-width">
                  <tr>
                    <td valign="top" class="header-cell">
                        <a href="http://www.georgebelanger.com"
                        style="background-color:#eeeeee;color:#03bb03;display:inline-block;font-family:sans-serif;font-size:32px;line-height:60px;text-align:center;text-decoration:none;width:250px;-webkit-text-size-adjust:none;">George Belanger</a>
                    </td>
                  </tr>
                  <tr>
                    <td valign="top" class="body-cell headlines">

                        <b>Dear {{first-name}}</b><br/>
                        <br/>
                        I just applied for {{job position}} at {{company}} and wanted to reach out to someone at the company because {{reason for enthusiasm}}. If you could forward this email to the right person, I would greatly appreciate it!<br/>
                        <br/>
                        Here's what makes me a perfect candidate for this position:<br/>
                        - {{reason one}}<br/>
                        - {{reason two}}<br/>
                        - {{reason three}}<br/>
                        <br/>
                        Some of my personal qualities which you may find useful for this role are:<br/>
                        -  Strong communication with technical and non-technical co-workers<br/>
                        -  Life-long learner with emphasis on books and podcasts<br/>
                        -  Hard working and spend 2 hours freelancing after full time job
                        <br/>
                        <br/>
                        <br/>
                      <table cellspacing="0" cellpadding="0" width="100%" bgcolor="#ffffff">
                          <tr>
                            <td style="width:200px;background:#03bb03;">
                              <div><!--[if mso]>
                                <v:rect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:40px;v-text-anchor:middle;width:200px;" stroke="f" fillcolor="#03bb03">
                                  <w:anchorlock/>
                                  <center>
                                <![endif]-->
                                    <a href="http://www.georgebelanger.com"
                              style="background-color:#03bb03;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:18px;line-height:40px;text-align:center;text-decoration:none;width:250px;-webkit-text-size-adjust:none;">View Portfolio</a>
                                <!--[if mso]>
                                  </center>
                                </v:rect>
                              <![endif]--></div>
                            </td>
                            <td width="360" style="background-color:#ffffff; font-size:0; line-height:0;">&nbsp;</td>
                            <td style="width:200px;background:#03bb03;">
                                <div><!--[if mso]>
                                  <v:rect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:40px;v-text-anchor:middle;width:200px;" stroke="f" fillcolor="#03bb03">
                                    <w:anchorlock/>
                                    <center>
                                  <![endif]-->
                                      <a href="https://docs.google.com/document/d/1PP4NuqfVHf5CSl8WMJjxCY_E3U2iIEZ_9HPhz0O3hc8/edit?usp=sharing"
                                style="background-color:#616060;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:18px;line-height:40px;text-align:center;text-decoration:none;width:250px;-webkit-text-size-adjust:none;">View Resume</a>
                                  <!--[if mso]>
                                    </center>
                                  </v:rect>
                                <![endif]--></div>
                              </td>
                          </tr>
                          
                        </table>
                        <br/>
                        <br/>
                        <table cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                              <td valign="top">
                                <table cellpadding="0" cellspacing="0" width="100%" class="progress progress-completed">
                                  <tr>
                                    <td valign="top" class="progress-marker">
                                      <img class="block-img" alt="" src="https://www.filepicker.io/api/file/J51uFVbhRfOe7VkurMgD" width="24" height="41">
                                    </td>
                                    <td valign="top" class="progress-title">
                                      <h1>Application Sent</h1>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td valign="top">
                                <table cellpadding="0" cellspacing="0" width="100%" class="progress progress-active">
                                  <tr>
                                    <td valign="top" colspan="3" class="progress-marker">
                                      <img alt="" class="block-img" src="https://www.filepicker.io/api/file/KYzgoHxSQEioFO9U4Cwe" width="24" height="35">
                                    </td>
                                    <td valign="top" class="progress-title">
                                      <h1>Phone Screen</h1>
                                    </td>
                                  </tr>
                                  <tr>
                                    <td valign="top" class="progress-line-pad">
                                    </td>
                                    <td valign="top" class="progress-line">
                                    </td>
                                    <td valign="top" class="progress-line-pad">
                                    </td>
                                    <td valign="top" class="progress-text">
                                      I want to find out more about {{company}} and how I can bring value to the company.
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td valign="top">
                                <table cellpadding="0" cellspacing="0" width="100%" class="progress progress-pending">
                                  <tr>
                                    <td valign="top" class="progress-marker">
                                      <img alt="" class="block-img" src="https://www.filepicker.io/api/file/DjQh9hYRXm4rx6j7uH0V" width="24" height="31">
                                    </td>
                                    <td valign="top" class="progress-title">
                                      <h1>Next steps</h1>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                          <br/>
                          <br/>
                          <b>Thank you very much!</b>
                    </td>
                  </tr>
                  <tr>
                    <td valign="top" class="footer-cell">
                      <img src="handset_round-2-512.png" height="14px" width="14px"> (207)572-3632  <br/>
                      <img src="ck_address_1181112.png" height="14px" width="14px"> Portland, Maine  <br/>
                      <a href="http://www.georgebelanger.com"> <img src="website-icon-8.png" height="14px" width="14px"> GeorgeBelanger.com </a> <br/>
                      <a href="https://www.linkedin.com/in/realtorgeorgeb"> <img src="linkedin.png" height="14px" width="14px"> linkedin.com/in/realtorgeorgeb</a> </br>
                      <a href="https://www.github.com/georgebelanger"> <img src="1024px-Octicons-mark-github.svg.png" height="14px" width="14px"> github.com/georgebelanger</a> <br/>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </center>
      </td>
    </tr>
  </table>

</body>
</html>

"""))